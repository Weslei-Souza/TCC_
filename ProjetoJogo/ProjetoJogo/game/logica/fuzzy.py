"""
Sistema de inferência fuzzy responsável por determinar
o nível de assistência oferecido pelo NPC.

ENTRADA 1
Necessidade de Assistência: 0 a 100
- baixa
- media
- alta

ENTRADA 2
Disposição Afetiva do NPC: 0 a 100
- hostil
- neutro
- amigavel

SAÍDA
Nível de Assistência: 0 a 100
- nenhuma
- generica
- intermediaria
- especifica

O sistema utiliza:

1. fuzzificação das duas entradas;
2. inferência Mamdani;
3. operador AND pelo mínimo;
4. agregação pelo máximo;
5. defuzzificação pelo centroide;
6. seleção do conjunto com maior pertinência
   no valor crisp resultante.
"""


# ============================================================
# FUNÇÕES DE PERTINÊNCIA BÁSICAS
# ============================================================

def triangular(x, a, b, c):
    """
    Função de pertinência triangular.

    a = início do conjunto
    b = ponto de pertinência máxima (1)
    c = final do conjunto

            1
            /\
           /  \
          /    \
    0 ---a--b--c--->
    """

    if x <= a or x >= c:
        return 0.0

    if x == b:
        return 1.0

    if x < b:
        return (x - a) / (b - a)

    return (c - x) / (c - b)


def trapezoidal(x, a, b, c, d):
    """
    Função de pertinência trapezoidal.

    Entre b e c a pertinência é máxima.

            ______
           /      \
          /        \
    0 ---a-b------c-d--->
    """

    if x < a or x > d:
        return 0.0

    if b <= x <= c:
        return 1.0

    if a <= x < b:

        if b == a:
            return 1.0

        return (x - a) / (b - a)

    if c < x <= d:

        if d == c:
            return 1.0

        return (d - x) / (d - c)

    return 0.0


# ============================================================
# FUZZIFICAÇÃO DA NECESSIDADE DE ASSISTÊNCIA
# ============================================================

def pertinencia_necessidade(valor):
    """
    Transforma o valor crisp da Necessidade de Assistência
    em graus de pertinência nos conjuntos:

    baixa
    media
    alta

    Um mesmo valor pode pertencer parcialmente
    a mais de um conjunto.
    """

    valor = max(
        0.0,
        min(float(valor), 100.0)
    )

    return {

        "baixa": trapezoidal(
            valor,
            0, 0, 25, 45
        ),

        "media": triangular(
            valor,
            30, 50, 70
        ),

        "alta": trapezoidal(
            valor,
            55, 75, 100, 100
        ),
    }


# ============================================================
# FUZZIFICAÇÃO DA DISPOSIÇÃO AFETIVA
# ============================================================

def pertinencia_disposicao(valor):
    """
    Transforma a Disposição do NPC em graus de pertinência:

    hostil
    neutro
    amigavel

    Esta é a classificação fuzzy.

    Ela é diferente da classificação narrativa simples
    usada pelo Navegador no início do encontro.
    """

    valor = max(
        0.0,
        min(float(valor), 100.0)
    )

    return {

        "hostil": trapezoidal(
            valor,
            0, 0, 25, 45
        ),

        "neutro": triangular(
            valor,
            30, 50, 70
        ),

        "amigavel": trapezoidal(
            valor,
            55, 75, 100, 100
        ),
    }


# ============================================================
# CONJUNTOS FUZZY DA SAÍDA
# ============================================================

def pertinencia_saida(valor):
    """
    Define os quatro níveis possíveis de assistência.

    O valor final ainda é fuzzy e pode possuir pertinência
    simultânea em conjuntos vizinhos.
    """

    valor = max(
        0.0,
        min(float(valor), 100.0)
    )

    return {

        "nenhuma": trapezoidal(
            valor,
            0, 0, 15, 30
        ),

        "generica": triangular(
            valor,
            20, 40, 55
        ),

        "intermediaria": triangular(
            valor,
            45, 65, 80
        ),

        "especifica": trapezoidal(
            valor,
            70, 85, 100, 100
        ),
    }


# ============================================================
# BASE DE REGRAS
# ============================================================

# Cada regra relaciona:
#
# Necessidade + Disposição -> Nível de Assistência

REGRAS = {

    # Necessidade baixa
    ("baixa", "hostil"): "nenhuma",
    ("baixa", "neutro"): "nenhuma",
    ("baixa", "amigavel"): "generica",

    # Necessidade média
    ("media", "hostil"): "nenhuma",
    ("media", "neutro"): "generica",
    ("media", "amigavel"): "intermediaria",

    # Necessidade alta
    ("alta", "hostil"): "generica",
    ("alta", "neutro"): "intermediaria",
    ("alta", "amigavel"): "especifica",
}


# ============================================================
# INFERÊNCIA DAS REGRAS
# ============================================================

def calcular_ativacoes(necessidade, disposicao):
    """
    Avalia as nove regras fuzzy.

    O operador AND é implementado pelo mínimo:

    ativacao_regra =
        min(pertinencia_necessidade,
            pertinencia_disposicao)

    Se mais de uma regra produz a mesma categoria de saída,
    fica a maior ativação encontrada.
    """

    graus_necessidade = pertinencia_necessidade(
        necessidade
    )

    graus_disposicao = pertinencia_disposicao(
        disposicao
    )

    ativacoes_saida = {
        "nenhuma": 0.0,
        "generica": 0.0,
        "intermediaria": 0.0,
        "especifica": 0.0,
    }

    for (
        conjunto_necessidade,
        conjunto_disposicao
    ), conjunto_saida in REGRAS.items():

        ativacao = min(
            graus_necessidade[conjunto_necessidade],
            graus_disposicao[conjunto_disposicao]
        )

        ativacoes_saida[conjunto_saida] = max(
            ativacoes_saida[conjunto_saida],
            ativacao
        )

    return ativacoes_saida


# ============================================================
# AGREGAÇÃO DA SAÍDA
# ============================================================

def pertinencia_agregada_saida(x, ativacoes):
    """
    Aplica a inferência Mamdani às funções da saída.

    Para cada categoria:

    1. calcula a pertinência original de x;
    2. corta essa pertinência no nível de ativação da regra
       usando o operador mínimo;
    3. agrega todos os conjuntos usando o operador máximo.
    """

    graus_saida = pertinencia_saida(x)

    valores_cortados = []

    for categoria, grau_original in graus_saida.items():

        grau_cortado = min(
            grau_original,
            ativacoes[categoria]
        )

        valores_cortados.append(
            grau_cortado
        )

    return max(valores_cortados)


# ============================================================
# DEFUZZIFICAÇÃO PELO CENTROIDE
# ============================================================

def defuzzificar(ativacoes):
    """
    Converte a saída fuzzy agregada em um único número.

    É utilizado o método do centroide:

        soma(x * pertinencia(x))
        ------------------------
          soma(pertinencia(x))

    O universo 0–100 é discretizado em valores inteiros.
    """

    numerador = 0.0
    denominador = 0.0

    for x in range(0, 101):

        grau = pertinencia_agregada_saida(
            x,
            ativacoes
        )

        numerador += x * grau
        denominador += grau

    if denominador == 0:
        return 0.0

    return numerador / denominador


# ============================================================
# TRANSFORMAR A SAÍDA NUMÉRICA EM CATEGORIA
# ============================================================

def escolher_categoria_saida(valor_saida):
    """
    O centroide produz um valor crisp.

    Exemplo:
        61.7

    Esse valor pode continuar pertencendo parcialmente
    a dois conjuntos.

    O jogo precisa escolher uma ação concreta, então
    selecionamos o conjunto no qual o valor possui
    MAIOR grau de pertinência.

    Em empate, prevalece o nível de menor assistência.
    """

    graus = pertinencia_saida(
        valor_saida
    )

    ordem = [
        "nenhuma",
        "generica",
        "intermediaria",
        "especifica",
    ]

    melhor_categoria = ordem[0]
    melhor_grau = graus[melhor_categoria]

    for categoria in ordem[1:]:

        if graus[categoria] > melhor_grau:

            melhor_categoria = categoria
            melhor_grau = graus[categoria]

    return melhor_categoria, graus


# ============================================================
# EXECUÇÃO COMPLETA DO SISTEMA FUZZY
# ============================================================

def calcular_assistencia(necessidade, disposicao):
    """
    Executa o processo completo:

    1. fuzzifica Necessidade;
    2. fuzzifica Disposição;
    3. executa as regras;
    4. agrega as saídas;
    5. defuzzifica pelo centroide;
    6. escolhe a categoria final.

    Retorna também os valores intermediários para que
    posteriormente possamos validar e explicar o sistema.
    """

    graus_necessidade = pertinencia_necessidade(
        necessidade
    )

    graus_disposicao = pertinencia_disposicao(
        disposicao
    )

    ativacoes = calcular_ativacoes(
        necessidade,
        disposicao
    )

    valor_saida = defuzzificar(
        ativacoes
    )

    categoria, graus_saida = escolher_categoria_saida(
        valor_saida
    )

    return {
        "valor": round(valor_saida, 2),
        "categoria": categoria,
        "necessidade": graus_necessidade,
        "disposicao": graus_disposicao,
        "ativacoes": ativacoes,
        "saida": graus_saida,
    }
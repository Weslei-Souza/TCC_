"""
Sistema fuzzy responsável por determinar o nível
de assistência oferecido pelo NPC.

Entradas:

1. Necessidade de Assistência
   - baixa
   - media
   - alta

2. Disposição do NPC
   - hostil
   - neutro
   - amigavel

Saída:

Nível de Assistência
   - nenhuma
   - generica
   - intermediaria
   - especifica

Universo de discurso das entradas e saída:
0 a 100.
"""


# ============================================================
# FUNÇÕES DE PERTINÊNCIA
# ============================================================

def triangular(x, a, b, c):
    """
    Função de pertinência triangular.
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
# NECESSIDADE DE ASSISTÊNCIA
# ============================================================

def pertinencia_necessidade(valor):
    """
    Calcula os graus de pertinência da Necessidade
    de Assistência.
    """

    valor = max(
        0.0,
        min(float(valor), 100.0)
    )


    return {

        "baixa": trapezoidal(
            valor,
            0,
            0,
            25,
            45
        ),

        "media": triangular(
            valor,
            30,
            50,
            70
        ),

        "alta": trapezoidal(
            valor,
            55,
            75,
            100,
            100
        ),
    }


# ============================================================
# DISPOSIÇÃO DO NPC
# ============================================================

def pertinencia_disposicao(valor):
    """
    Calcula os graus de pertinência da
    Disposição Afetiva do NPC.
    """

    valor = max(
        0.0,
        min(float(valor), 100.0)
    )


    return {

        "hostil": trapezoidal(
            valor,
            0,
            0,
            25,
            45
        ),

        "neutro": triangular(
            valor,
            30,
            50,
            70
        ),

        "amigavel": trapezoidal(
            valor,
            55,
            75,
            100,
            100
        ),
    }


# ============================================================
# SAÍDA - NÍVEL DE ASSISTÊNCIA
# ============================================================

def pertinencia_saida(valor):
    """
    Calcula os graus de pertinência da saída fuzzy.
    """

    valor = max(
        0.0,
        min(float(valor), 100.0)
    )


    return {

        "nenhuma": trapezoidal(
            valor,
            0,
            0,
            15,
            30
        ),

        "generica": triangular(
            valor,
            20,
            40,
            55
        ),

        "intermediaria": triangular(
            valor,
            45,
            65,
            80
        ),

        "especifica": trapezoidal(
            valor,
            70,
            85,
            100,
            100
        ),
    }


# ============================================================
# BASE DE REGRAS
# ============================================================

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
# EXECUÇÃO DAS REGRAS
# ============================================================

def calcular_ativacoes(
    necessidade,
    disposicao
):
    """
    Calcula a ativação de cada conjunto de saída
    usando operador AND = mínimo.

    Quando mais de uma regra produz a mesma saída,
    utilizamos o máximo das ativações.
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
            graus_necessidade[
                conjunto_necessidade
            ],
            graus_disposicao[
                conjunto_disposicao
            ]
        )


        ativacoes_saida[
            conjunto_saida
        ] = max(
            ativacoes_saida[
                conjunto_saida
            ],
            ativacao
        )


    return ativacoes_saida


# ============================================================
# AGREGAÇÃO DA SAÍDA
# ============================================================

def pertinencia_agregada_saida(
    x,
    ativacoes
):
    """
    Aplica o corte das funções de saída de acordo
    com a ativação das regras e agrega os resultados
    pelo operador máximo.
    """

    graus_saida = pertinencia_saida(
        x
    )


    valores_cortados = []


    for categoria, grau_original in graus_saida.items():

        grau_cortado = min(
            grau_original,
            ativacoes[categoria]
        )

        valores_cortados.append(
            grau_cortado
        )


    return max(
        valores_cortados
    )


# ============================================================
# DEFUZZIFICAÇÃO
# ============================================================

def defuzzificar(ativacoes):
    """
    Realiza a defuzzificação pelo método do centroide.

    O universo de saída é discretizado de 0 a 100.
    """

    numerador = 0.0

    denominador = 0.0


    for x in range(0, 101):

        grau = pertinencia_agregada_saida(
            x,
            ativacoes
        )


        numerador += (
            x * grau
        )

        denominador += grau


    if denominador == 0:

        return 0.0


    return numerador / denominador


# ============================================================
# ESCOLHER CATEGORIA DA DICA
# ============================================================

def escolher_categoria_saida(
    valor_saida
):
    """
    Após a defuzzificação, verifica em qual conjunto
    o valor crisp possui maior grau de pertinência.

    Em caso de empate, a opção de menor assistência
    é priorizada.
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

    melhor_grau = graus[
        melhor_categoria
    ]


    for categoria in ordem[1:]:

        if graus[categoria] > melhor_grau:

            melhor_categoria = categoria

            melhor_grau = graus[
                categoria
            ]


    return melhor_categoria, graus


# ============================================================
# SISTEMA FUZZY COMPLETO
# ============================================================

def calcular_assistencia(
    necessidade,
    disposicao
):
    """
    Executa todo o sistema fuzzy.

    Retorna:

    - valor crisp da saída;
    - categoria escolhida;
    - graus das entradas;
    - ativações das regras;
    - graus da saída final.

    Esses dados adicionais serão úteis nos testes
    e na validação do modelo.
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

        "valor": round(
            valor_saida,
            2
        ),

        "categoria": categoria,

        "necessidade": graus_necessidade,

        "disposicao": graus_disposicao,

        "ativacoes": ativacoes,

        "saida": graus_saida,
    }
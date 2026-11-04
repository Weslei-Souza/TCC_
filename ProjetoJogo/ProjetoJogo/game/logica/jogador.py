"""
Funções e parâmetros relacionados às métricas do jogador.

Este módulo não armazena diretamente o estado da partida.
Ele recebe dados do Ren'Py, processa essas informações
e devolve os resultados.
"""


# ============================================================
# PESOS DA NECESSIDADE DE ASSISTÊNCIA
# ============================================================

PESOS_NECESSIDADE_ASSISTENCIA = {

    "reinicios": 0.35,

    "dicas_pedidas": 0.25,

    "estados_repetidos": 0.15,

    "armadilhas": 0.25,
}


# ============================================================
# NORMALIZAÇÃO DE UMA MÉTRICA
# ============================================================

def normalizar_metrica(valor, limite):
    """
    Normaliza uma métrica para o intervalo entre 0 e 1.

    O limite representa o valor de referência a partir
    do qual a métrica é considerada máxima para o cálculo.

    Exemplo:

    valor = 2
    limite = 3

    resultado = 0.666...

    Valores acima do limite permanecem em 1.
    """

    if limite is None:
        return None


    if limite <= 0:
        return 0.0


    valor_normalizado = valor / limite


    return min(
        max(valor_normalizado, 0.0),
        1.0
    )


# ============================================================
# NECESSIDADE DE ASSISTÊNCIA
# ============================================================

def calcular_necessidade_assistencia(
    reinicios,
    dicas_pedidas,
    estados_repetidos,
    armadilhas,
    limites
):
    """
    Calcula a Necessidade de Assistência do jogador.

    As métricas são:

    - normalizadas;
    - multiplicadas por seus respectivos pesos;
    - combinadas por média ponderada.

    Métricas não aplicáveis à fase devem possuir
    limite igual a None e são retiradas do cálculo.

    Retorna um valor entre 0 e 100.
    """

    valores = {

        "reinicios": reinicios,

        "dicas_pedidas": dicas_pedidas,

        "estados_repetidos": estados_repetidos,

        "armadilhas": armadilhas,
    }


    soma_ponderada = 0.0

    soma_pesos_ativos = 0.0


    for metrica, valor in valores.items():

        limite = limites.get(metrica)


        # Métrica inexistente nesta fase.
        if limite is None:
            continue


        valor_normalizado = normalizar_metrica(
            valor,
            limite
        )


        peso = PESOS_NECESSIDADE_ASSISTENCIA[
            metrica
        ]


        soma_ponderada += (
            valor_normalizado * peso
        )


        soma_pesos_ativos += peso


    # Proteção para o caso de uma fase não possuir
    # nenhuma métrica configurada.

    if soma_pesos_ativos == 0:

        return 0.0


    necessidade = (
        soma_ponderada
        / soma_pesos_ativos
    ) * 100


    return round(
        necessidade,
        2
    )


# ============================================================
# REGISTRO DO PERCURSO
# ============================================================

def registrar_percurso(
    historico_atual,
    novos_estados
):
    """
    Registra os estados visitados pelo jogador.

    Retorna:

    - histórico atualizado;
    - quantidade de estados repetidos encontrados.
    """

    historico = list(
        historico_atual
    )


    repeticoes = 0


    for estado in novos_estados:

        if estado in historico:

            repeticoes += 1


        historico.append(
            estado
        )


    return historico, repeticoes
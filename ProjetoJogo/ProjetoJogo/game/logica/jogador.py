"""
Funções e parâmetros relacionados às métricas do jogador.

Este módulo não armazena diretamente o estado da partida.
Ele recebe dados do Ren'Py, processa essas informações
e devolve os resultados.
"""


# ============================================================
# PESOS DA NECESSIDADE DE ASSISTÊNCIA
# ============================================================

# Os pesos somam 1.0.
#
# A fórmula final ainda NÃO é calculada neste módulo,
# pois primeiro será necessário definir como cada métrica
# será normalizada.

PESOS_NECESSIDADE_ASSISTENCIA = {

    "reinicios": 0.35,

    "dicas_pedidas": 0.25,

    "estados_repetidos": 0.15,

    "armadilhas": 0.25,
}


# ============================================================
# POTENCIALIZADOR POR TENTATIVA
# ============================================================

def potencializador_tentativa(numero_tentativas):
    """
    Retorna o percentual que futuramente será aplicado
    sobre a Necessidade de Assistência calculada.

    Tentativa 1  -> +0%
    Tentativa 2  -> +10%
    Tentativa 3  -> +25%
    Tentativa 4+ -> +50%
    """

    if numero_tentativas <= 1:
        return 0.0

    if numero_tentativas == 2:
        return 0.10

    if numero_tentativas == 3:
        return 0.25

    return 0.50


# ============================================================
# REGISTRO DO PERCURSO
# ============================================================

def registrar_percurso(historico_atual, novos_estados):
    """
    Registra os estados visitados pelo jogador.

    Retorna:

    - histórico atualizado;
    - quantidade de estados repetidos encontrados.
    """

    historico = list(historico_atual)

    repeticoes = 0


    for estado in novos_estados:

        # Se o estado já havia aparecido anteriormente,
        # contabilizamos uma repetição.

        if estado in historico:
            repeticoes += 1

        historico.append(estado)


    return historico, repeticoes
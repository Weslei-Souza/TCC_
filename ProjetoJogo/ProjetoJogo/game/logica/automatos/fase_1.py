"""
Configuração do autômato utilizado na Fase 1.

Este arquivo contém somente os dados específicos
desta fase.

A lógica de processamento permanece em:

logica/automato.py
"""


# ============================================================
# ALFABETO
# ============================================================

ALFABETO = {
    "A",
    "B",
}


# ============================================================
# ESTADO INICIAL
# ============================================================

ESTADO_INICIAL = "q0"


# ============================================================
# ESTADOS FINAIS
# ============================================================

ESTADOS_FINAIS = {
    "qf"
}


# ============================================================
# NOMES DOS ESTADOS
# ============================================================

NOMES_ESTADOS = {

    "q0": "Ilha 1",

    "q1": "Ilha 2",

    "q2": "Ilha 3",

    "qf": "Ilha Final",
}


# ============================================================
# FUNÇÃO DE TRANSIÇÃO
# ============================================================

TRANSICOES = {

    "q0": {
        "A": "q1",
        "B": "q2",
    },

    "q1": {
        "A": "q0",
        "B": "q2",
    },

    "q2": {
        "A": "q0",
        "B": "qf",
    },

    # O estado final funciona como estado absorvente.
    #
    # Mesmo que o jogo encerre a fase quando qf é atingido,
    # formalmente cada símbolo continua possuindo
    # uma transição definida.

    "qf": {
        "A": "qf",
        "B": "qf",
    },
}


# ============================================================
# CONFIGURAÇÃO
# ============================================================

CONFIGURACAO = {

    "alfabeto": ALFABETO,

    "estado_inicial": ESTADO_INICIAL,

    "estados_finais": ESTADOS_FINAIS,

    "nomes_estados": NOMES_ESTADOS,

    "transicoes": TRANSICOES,
}
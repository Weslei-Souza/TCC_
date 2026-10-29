"""
Configuração do autômato utilizado na Fase 1.

Este arquivo contém somente os dados específicos
desta fase.

A lógica de processamento do autômato permanece
em logica/automato.py.
"""


ESTADO_INICIAL = "q0"


ESTADOS_FINAIS = {
    "qf"
}


NOMES_ESTADOS = {
    "q0": "Ilha 1",
    "q1": "Ilha 2",
    "q2": "Ilha 3",
    "qf": "Ilha Final",
}


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

    "qf": {}
}


CONFIGURACAO = {
    "estado_inicial": ESTADO_INICIAL,
    "estados_finais": ESTADOS_FINAIS,
    "nomes_estados": NOMES_ESTADOS,
    "transicoes": TRANSICOES,
}
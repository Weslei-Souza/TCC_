"""
Configuração lógica da Fase 2.

Novidade principal:
múltiplos caminhos e retornos entre ilhas.
"""


NUMERO_FASE = 2
NOME_FASE = "Fase 2"


ALFABETO = {
    "A",
    "B",
}


ESTADO_INICIAL = "q0"


ESTADOS_FINAIS = {
    "qf",
}


ESTADOS_ARMADILHA = set()


NOMES_ESTADOS = {

    "q0": "Ilha 1",
    "q1": "Ilha 2",
    "q2": "Ilha 3",
    "q3": "Ilha 4",
    "q4": "Ilha 5",
    "qf": "Ilha Final",
}


TRANSICOES = {

    "q0": {
        "A": "q1",
        "B": "q2",
    },

    "q1": {
        "A": "q2",
        "B": "q3",
    },

    "q2": {
        "A": "q4",
        "B": "q0",
    },

    "q3": {
        "A": "q0",
        "B": "q4",
    },

    "q4": {
        "A": "q3",
        "B": "qf",
    },

    "qf": {
        "A": "qf",
        "B": "qf",
    },
}


LIMITES_ASSISTENCIA = {

    "reinicios": 3,
    "dicas_pedidas": 3,
    "estados_repetidos": 4,
    "armadilhas": None,
}


CONFIGURACAO_NPC = {

    "modo": "aleatorio",
    "estado_fixo": None,
    "chance_encontro": 0.50,
    "max_encontros": 2,
}


CONFIGURACAO = {

    "numero_fase": NUMERO_FASE,
    "nome_fase": NOME_FASE,

    "alfabeto": ALFABETO,

    "estado_inicial": ESTADO_INICIAL,
    "estados_finais": ESTADOS_FINAIS,
    "estados_armadilha": ESTADOS_ARMADILHA,

    "nomes_estados": NOMES_ESTADOS,
    "transicoes": TRANSICOES,

    "limites_assistencia": LIMITES_ASSISTENCIA,

    "npc": CONFIGURACAO_NPC,
}
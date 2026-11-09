"""
Configuração lógica da Fase 5.

Primeiro desafio integrado.

Combina:
- múltiplos caminhos;
- retornos;
- redemoinho;
- prisão.
"""


NUMERO_FASE = 5
NOME_FASE = "Fase 5"


ALFABETO = {
    "A",
    "B",
}


ESTADO_INICIAL = "q0"


ESTADOS_FINAIS = {
    "qf",
}


ESTADOS_ARMADILHA = {
    "qd",
}


NOMES_ESTADOS = {

    "q0": "Ilha 1",
    "q1": "Ilha 2",
    "q2": "Ilha 3",
    "q3": "Ilha 4",
    "q4": "Ilha 5",
    "q5": "Ilha 6",

    "qd": "Prisão",

    "qf": "Ilha do Tesouro",
}


TRANSICOES = {

    "q0": {
        "A": "q1",
        "B": "q2",
    },

    "q1": {
        "A": "q3",
        "B": "q4",
    },

    "q2": {
        "A": "q4",
        "B": "q0",
    },

    # Redemoinho.
    "q3": {
        "A": "q3",
        "B": "q5",
    },

    "q4": {
        "A": "qd",
        "B": "q5",
    },

    "q5": {
        "A": "qd",
        "B": "qf",
    },

    "qd": {
        "A": "qd",
        "B": "qd",
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
    "armadilhas": 2,
}


CONFIGURACAO_NPC = {

    "modo": "aleatorio",
    "estado_fixo": None,
    "chance_encontro": 0.60,
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
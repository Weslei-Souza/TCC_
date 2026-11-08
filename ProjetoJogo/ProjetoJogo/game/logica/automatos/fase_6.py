"""
Configuração lógica da Fase 6.

Desafio avançado com:
- caminhos alternativos;
- ciclos;
- auto-laço;
- duas prisões;
- maior profundidade.
"""


NUMERO_FASE = 6
NOME_FASE = "Fase 6"


ALFABETO = {
    "A",
    "B",
}


ESTADO_INICIAL = "q0"


ESTADOS_FINAIS = {
    "qf",
}


ESTADOS_ARMADILHA = {
    "qd1",
    "qd2",
}


NOMES_ESTADOS = {

    "q0": "Ilha 1",
    "q1": "Ilha 2",
    "q2": "Ilha 3",
    "q3": "Ilha 4",
    "q4": "Ilha 5",
    "q5": "Ilha 6",
    "q6": "Ilha 7",

    "qd1": "Prisão 1",
    "qd2": "Prisão 2",

    "qf": "Ilha Final",
}


TRANSICOES = {

    "q0": {
        "A": "q1",
        "B": "q2",
    },

    "q1": {
        "A": "q1",
        "B": "q3",
    },

    "q2": {
        "A": "q4",
        "B": "q0",
    },

    "q3": {
        "A": "qd1",
        "B": "q5",
    },

    "q4": {
        "A": "q5",
        "B": "qd2",
    },

    "q5": {
        "A": "q6",
        "B": "qd1",
    },

    "q6": {
        "A": "qd2",
        "B": "qf",
    },

    "qd1": {
        "A": "qd1",
        "B": "qd1",
    },

    "qd2": {
        "A": "qd2",
        "B": "qd2",
    },

    "qf": {
        "A": "qf",
        "B": "qf",
    },
}


LIMITES_ASSISTENCIA = {

    "reinicios": 4,
    "dicas_pedidas": 4,
    "estados_repetidos": 5,
    "armadilhas": 3,
}


CONFIGURACAO_NPC = {

    "modo": "aleatorio",
    "estado_fixo": None,
    "chance_encontro": 0.65,
    "max_encontros": 3,
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
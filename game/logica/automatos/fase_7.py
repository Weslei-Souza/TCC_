"""
Configuração lógica da Fase 7.

Desafio final.

Combina todos os elementos introduzidos anteriormente:
- caminhos alternativos;
- retornos;
- ciclos;
- três redemoinhos;
- duas prisões;
- sequência de navegação mais longa.
"""


NUMERO_FASE = 7
NOME_FASE = "Fase 7"


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
    "q7": "Ilha 8",
    "q8": "Ilha 9",

    "qd1": "Prisão 1",
    "qd2": "Prisão 2",

    "qf": "Ilha do Tesouro",
}


TRANSICOES = {

    "q0": {
        "A": "q1",
        "B": "q2",
    },

    "q1": {
        "A": "q3",
        "B": "qd1",
    },

    # Redemoinho 1.
    "q2": {
        "A": "q2",
        "B": "q5",
    },

    "q3": {
        "A": "qd1",
        "B": "q6",
    },

    "q4": {
        "A": "q6",
        "B": "q1",
    },

    # Redemoinho 2.
    "q5": {
        "A": "q4",
        "B": "q5",
    },

    "q6": {
        "A": "q7",
        "B": "qd2",
    },

    # Redemoinho 3.
    "q7": {
        "A": "q7",
        "B": "q8",
    },

    "q8": {
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
    "estados_repetidos": 6,
    "armadilhas": 3,
}


CONFIGURACAO_NPC = {

    "modo": "aleatorio",
    "estado_fixo": None,
    "chance_encontro": 0.70,
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
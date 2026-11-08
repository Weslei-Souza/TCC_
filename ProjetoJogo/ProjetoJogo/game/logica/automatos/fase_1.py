"""
Configuração lógica da Fase 1.

Este arquivo contém somente dados específicos da fase.

A lógica de processamento permanece nos módulos gerais:
- automato.py
- jogador.py
- npc.py
- fuzzy.py
"""


# ============================================================
# IDENTIFICAÇÃO DA FASE
# ============================================================

NUMERO_FASE = 1

NOME_FASE = "Fase 1"


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
# ESTADO FINAL
# ============================================================

ESTADOS_FINAIS = {
    "qf"
}


# ============================================================
# ESTADOS DE ARMADILHA
# ============================================================

# A Fase 1 atual não possui armadilhas.
#
# Em fases futuras poderemos ter, por exemplo:
#
# ESTADOS_ARMADILHA = {
#     "q4"
# }

ESTADOS_ARMADILHA = set()


# ============================================================
# NOMES EXIBIDOS AO JOGADOR
# ============================================================

# Os identificadores q0, q1 etc. são usados apenas
# internamente.
#
# A interface utiliza os nomes definidos aqui.

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

    # O estado final permanece absorvente para que
    # o autômato continue completo.

    "qf": {
        "A": "qf",
        "B": "qf",
    },
}


# ============================================================
# LIMITES DA NECESSIDADE DE ASSISTÊNCIA
# ============================================================

# Valores provisórios da Fase 1.
#
# Serão redefinidos quando os autômatos definitivos
# das sete fases forem modelados.

LIMITES_ASSISTENCIA = {

    "reinicios": 3,

    "dicas_pedidas": 3,

    "estados_repetidos": 3,

    "armadilhas": None,
}


# ============================================================
# CONFIGURAÇÃO DOS ENCONTROS COM NPC
# ============================================================

# Modos possíveis:
#
# "nenhum"
# "fixo"
# "aleatorio"
#
# A Fase 1 atual utiliza um encontro tutorial fixo.

CONFIGURACAO_NPC = {

    "modo": "fixo",

    # Usado somente quando modo == "fixo".
    "estado_fixo": "q2",

    # Probabilidade entre 0.0 e 1.0.
    #
    # No modo fixo ela não é utilizada, mas mantemos
    # a chave para que todas as fases possuam a mesma
    # estrutura de configuração.
    "chance_encontro": 1.0,

    # Quantidade máxima de encontros durante
    # uma execução da fase.
    "max_encontros": 1,
}


# ============================================================
# CONFIGURAÇÃO COMPLETA
# ============================================================

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
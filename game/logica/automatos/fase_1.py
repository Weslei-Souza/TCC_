"""
Configuração lógica da Fase 1.

FASE 1 - TUTORIAL

Objetivo da fase:
apresentar ao jogador o funcionamento básico da navegação
entre estados utilizando as entradas A e B.

A fase possui:

- um estado inicial;
- uma ilha intermediária;
- um estado final;
- nenhuma armadilha;
- um encontro fixo com NPC.

Os identificadores q0, q1 e qf são utilizados apenas
internamente. A interface apresenta nomes de ilhas.
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
    "qf",
}


# ============================================================
# ESTADOS DE ARMADILHA
# ============================================================

# A Fase 1 não possui estados de armadilha.

ESTADOS_ARMADILHA = set()


# ============================================================
# NOMES EXIBIDOS AO JOGADOR
# ============================================================

NOMES_ESTADOS = {

    "q0": "Ilha 1",

    "q1": "Ilha 2",

    "qf": "Ilha do Tesouro",
}


# ============================================================
# FUNÇÃO DE TRANSIÇÃO
# ============================================================

# Cada estado possui exatamente uma transição
# para cada símbolo do alfabeto.
#
# Portanto, o autômato é determinístico e completo.

TRANSICOES = {

    # --------------------------------------------------------
    # q0 - ESTADO INICIAL
    # --------------------------------------------------------

    "q0": {

        "A": "q1",

        "B": "q1",
    },


    # --------------------------------------------------------
    # q1 - ILHA INTERMEDIÁRIA
    # --------------------------------------------------------

    # A devolve o jogador ao início.
    #
    # B leva ao estado final.

    "q1": {

        "A": "q0",

        "B": "qf",
    },


    # --------------------------------------------------------
    # qf - ESTADO FINAL
    # --------------------------------------------------------

    # Formalmente o autômato precisa possuir
    # transições também a partir do estado final.
    #
    # No jogo essas transições não são utilizadas,
    # pois a fase termina imediatamente ao chegar em qf.

    "qf": {

        "A": "qf",

        "B": "qf",
    },
}


# ============================================================
# LIMITES DA NECESSIDADE DE ASSISTÊNCIA
# ============================================================

# Estes limites determinam quando cada métrica normalizada
# atinge seu valor máximo.
#
# A Fase 1 não possui armadilhas, portanto essa métrica
# não participa da média ponderada.

LIMITES_ASSISTENCIA = {

    "reinicios": 3,

    "dicas_pedidas": 3,

    "estados_repetidos": 3,

    "armadilhas": None,
}


# ============================================================
# CONFIGURAÇÃO DO NPC
# ============================================================

# A primeira fase funciona como tutorial.
#
# Por isso o encontro não é aleatório.
# O Náufrago aparece obrigatoriamente na Ilha 2 (q1).

CONFIGURACAO_NPC = {

    "modo": "fixo",

    "estado_fixo": "q1",

    # Não é utilizada no modo fixo,
    # mas permanece definida porque faz parte
    # do contrato genérico das fases.

    "chance_encontro": 1.0,

    # O encontro tutorial acontece apenas uma vez
    # por execução da fase.

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
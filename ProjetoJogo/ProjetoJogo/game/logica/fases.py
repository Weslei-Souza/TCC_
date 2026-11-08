"""
Registro e validação das fases do jogo.

Este módulo faz a ligação entre o número da fase
selecionada pelo jogador e sua configuração lógica.
"""


from logica import automato

from logica.automatos import fase_1


# ============================================================
# REGISTRO DAS FASES IMPLEMENTADAS
# ============================================================

# Somente fases efetivamente implementadas devem entrar
# neste dicionário.
#
# Conforme criarmos as próximas:
#
# 2: fase_2.CONFIGURACAO
# 3: fase_3.CONFIGURACAO
# ...

FASES = {

    1: fase_1.CONFIGURACAO,
}


# ============================================================
# CHAVES OBRIGATÓRIAS DE UMA FASE
# ============================================================

CHAVES_OBRIGATORIAS = {

    "numero_fase",

    "nome_fase",

    "alfabeto",

    "estado_inicial",

    "estados_finais",

    "estados_armadilha",

    "nomes_estados",

    "transicoes",

    "limites_assistencia",

    "npc",
}


# ============================================================
# VERIFICAR SE UMA FASE ESTÁ IMPLEMENTADA
# ============================================================

def fase_implementada(numero_fase):

    return numero_fase in FASES


# ============================================================
# LISTAR FASES IMPLEMENTADAS
# ============================================================

def fases_implementadas():

    return sorted(
        FASES.keys()
    )


# ============================================================
# VALIDAR CONFIGURAÇÃO DA FASE
# ============================================================

def validar_configuracao(configuracao):
    """
    Realiza verificações estruturais antes que uma fase
    seja utilizada pelo jogo.

    A função gera ValueError quando encontra uma
    configuração inconsistente.
    """


    # --------------------------------------------------------
    # CHAVES OBRIGATÓRIAS
    # --------------------------------------------------------

    faltando = (
        CHAVES_OBRIGATORIAS
        - set(configuracao.keys())
    )


    if faltando:

        raise ValueError(
            "Configuração da fase incompleta. "
            f"Chaves ausentes: {sorted(faltando)}"
        )


    # --------------------------------------------------------
    # ESTADOS CADASTRADOS
    # --------------------------------------------------------

    estados = set(
        configuracao["nomes_estados"].keys()
    )


    estado_inicial = configuracao[
        "estado_inicial"
    ]


    estados_finais = set(
        configuracao["estados_finais"]
    )


    estados_armadilha = set(
        configuracao["estados_armadilha"]
    )


    if estado_inicial not in estados:

        raise ValueError(
            "O estado inicial não está cadastrado "
            "em nomes_estados."
        )


    if not estados_finais:

        raise ValueError(
            "A fase precisa possuir pelo menos "
            "um estado final."
        )


    if not estados_finais.issubset(estados):

        raise ValueError(
            "Existe estado final não cadastrado "
            "em nomes_estados."
        )


    if not estados_armadilha.issubset(estados):

        raise ValueError(
            "Existe estado de armadilha não cadastrado "
            "em nomes_estados."
        )


    if estados_finais & estados_armadilha:

        raise ValueError(
            "Um mesmo estado não pode ser final "
            "e armadilha simultaneamente."
        )


    # --------------------------------------------------------
    # DETERMINISMO E COMPLETUDE
    # --------------------------------------------------------

    if not automato.validar_determinismo(
        configuracao
    ):

        raise ValueError(
            "O autômato da fase não é determinístico "
            "e completo para o alfabeto informado."
        )


    # --------------------------------------------------------
    # CONFIGURAÇÃO DO NPC
    # --------------------------------------------------------

    config_npc = configuracao["npc"]


    modo_npc = config_npc.get(
        "modo"
    )


    modos_validos = {
        "nenhum",
        "fixo",
        "aleatorio",
    }


    if modo_npc not in modos_validos:

        raise ValueError(
            f"Modo de NPC inválido: {modo_npc}"
        )


    chance = config_npc.get(
        "chance_encontro",
        0.0
    )


    if not 0.0 <= chance <= 1.0:

        raise ValueError(
            "chance_encontro deve estar "
            "entre 0.0 e 1.0."
        )


    max_encontros = config_npc.get(
        "max_encontros",
        0
    )


    if max_encontros < 0:

        raise ValueError(
            "max_encontros não pode ser negativo."
        )


    # --------------------------------------------------------
    # NPC FIXO
    # --------------------------------------------------------

    if modo_npc == "fixo":

        estado_fixo = config_npc.get(
            "estado_fixo"
        )


        if estado_fixo not in estados:

            raise ValueError(
                "O estado fixo do NPC não existe "
                "no autômato."
            )


        if not automato.eh_intermediario(
            configuracao,
            estado_fixo
        ):

            raise ValueError(
                "O NPC fixo precisa estar em um "
                "estado intermediário."
            )


    return True


# ============================================================
# OBTER CONFIGURAÇÃO DE UMA FASE
# ============================================================

def obter_configuracao(numero_fase):
    """
    Retorna a configuração da fase solicitada
    após validar sua estrutura.
    """


    if numero_fase not in FASES:

        raise ValueError(
            f"Fase {numero_fase} ainda não implementada."
        )


    configuracao = FASES[
        numero_fase
    ]


    validar_configuracao(
        configuracao
    )


    return configuracao


# ============================================================
# COMPATIBILIDADE COM O CÓDIGO ATUAL
# ============================================================

def obter_automato(numero_fase):
    """
    Mantém compatibilidade com o restante do projeto.

    Atualmente a configuração da fase já contém
    toda a configuração necessária ao autômato.
    """

    return obter_configuracao(
        numero_fase
    )
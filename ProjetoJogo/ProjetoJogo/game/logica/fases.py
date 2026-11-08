"""
Registro e validação das fases do jogo.

Este módulo faz a ligação entre o número da fase
selecionada pelo jogador e sua configuração lógica.
"""


from logica import automato

from logica.automatos import (
    fase_1,
    fase_2,
    fase_3,
    fase_4,
    fase_5,
    fase_6,
    fase_7,
)


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
# LIMITES OBRIGATÓRIOS
# ============================================================

LIMITES_OBRIGATORIOS = {

    "reinicios",

    "dicas_pedidas",

    "estados_repetidos",

    "armadilhas",
}


# ============================================================
# CONFIGURAÇÃO OBRIGATÓRIA DO NPC
# ============================================================

CHAVES_NPC_OBRIGATORIAS = {

    "modo",

    "estado_fixo",

    "chance_encontro",

    "max_encontros",
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


    # ========================================================
    # EXATAMENTE UM ESTADO FINAL
    # ========================================================

    if len(estados_finais) != 1:

        raise ValueError(
            "Cada fase deve possuir exatamente "
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
    # LIMITES DA NECESSIDADE DE ASSISTÊNCIA
    # --------------------------------------------------------

    limites = configuracao[
        "limites_assistencia"
    ]


    limites_faltando = (
        LIMITES_OBRIGATORIOS
        - set(limites.keys())
    )


    if limites_faltando:

        raise ValueError(
            "Limites de assistência incompletos. "
            f"Ausentes: {sorted(limites_faltando)}"
        )


    # --------------------------------------------------------
    # MÉTRICAS SEMPRE ATIVAS
    # --------------------------------------------------------

    metricas_obrigatorias = {

        "reinicios",

        "dicas_pedidas",

        "estados_repetidos",
    }


    for metrica in metricas_obrigatorias:

        limite = limites[
            metrica
        ]


        if (
            limite is None
            or not isinstance(
                limite,
                (int, float)
            )
            or isinstance(
                limite,
                bool
            )
            or limite <= 0
        ):

            raise ValueError(
                f"Limite inválido para {metrica}: "
                f"{limite}"
            )


    # --------------------------------------------------------
    # ARMADILHAS
    # --------------------------------------------------------

    limite_armadilhas = limites[
        "armadilhas"
    ]


    if estados_armadilha:

        # Se a fase possui armadilha,
        # essa métrica precisa estar ativa.

        if (
            limite_armadilhas is None
            or not isinstance(
                limite_armadilhas,
                (int, float)
            )
            or isinstance(
                limite_armadilhas,
                bool
            )
            or limite_armadilhas <= 0
        ):

            raise ValueError(
                "Fases com estados de armadilha precisam "
                "possuir um limite positivo para a métrica "
                "armadilhas."
            )


    else:

        # Se a fase não possui nenhuma armadilha,
        # ela deve ser retirada da média ponderada.

        if limite_armadilhas is not None:

            raise ValueError(
                "Fases sem armadilhas devem utilizar "
                "armadilhas = None nos limites de assistência."
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


    # --------------------------------------------------------
    # CHAVES OBRIGATÓRIAS
    # --------------------------------------------------------

    chaves_npc_faltando = (
        CHAVES_NPC_OBRIGATORIAS
        - set(config_npc.keys())
    )


    if chaves_npc_faltando:

        raise ValueError(
            "Configuração do NPC incompleta. "
            f"Ausentes: {sorted(chaves_npc_faltando)}"
        )


    # --------------------------------------------------------
    # MODO DO NPC
    # --------------------------------------------------------

    modo_npc = config_npc[
        "modo"
    ]


    modos_validos = {
        "nenhum",
        "fixo",
        "aleatorio",
    }


    if modo_npc not in modos_validos:

        raise ValueError(
            f"Modo de NPC inválido: {modo_npc}"
        )


    # --------------------------------------------------------
    # CHANCE DE ENCONTRO
    # --------------------------------------------------------

    chance = config_npc[
        "chance_encontro"
    ]


    if (
        not isinstance(
            chance,
            (int, float)
        )
        or isinstance(
            chance,
            bool
        )
        or not 0.0 <= chance <= 1.0
    ):

        raise ValueError(
            "chance_encontro deve ser um número "
            "entre 0.0 e 1.0."
        )


    # --------------------------------------------------------
    # MÁXIMO DE ENCONTROS
    # --------------------------------------------------------

    # IMPORTANTE:
    # precisamos criar esta variável ANTES de utilizá-la
    # nas verificações abaixo.

    max_encontros = config_npc[
        "max_encontros"
    ]


    if (
        not isinstance(
            max_encontros,
            int
        )
        or isinstance(
            max_encontros,
            bool
        )
        or max_encontros < 0
    ):

        raise ValueError(
            "max_encontros deve ser um "
            "número inteiro maior ou igual a zero."
        )


    # --------------------------------------------------------
    # COERÊNCIA DO MODO DE NPC
    # --------------------------------------------------------

    if modo_npc == "nenhum":

        if max_encontros != 0:

            raise ValueError(
                "Uma fase sem NPC deve possuir "
                "max_encontros = 0."
            )


    elif modo_npc == "fixo":

        if max_encontros < 1:

            raise ValueError(
                "Uma fase com NPC fixo precisa permitir "
                "pelo menos um encontro."
            )


    elif modo_npc == "aleatorio":

        if max_encontros < 1:

            raise ValueError(
                "Uma fase com NPC aleatório precisa permitir "
                "pelo menos um encontro."
            )


        if chance <= 0:

            raise ValueError(
                "Uma fase com NPC aleatório precisa possuir "
                "chance_encontro maior que zero."
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

    if configuracao["numero_fase"] != numero_fase:

        raise ValueError(
            "O número declarado na configuração da fase "
            "não corresponde ao número usado no registro."
        )


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
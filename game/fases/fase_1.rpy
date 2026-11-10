# ============================================================
# FASE 1
# TUTORIAL DE NAVEGAÇÃO
# ============================================================

# ============================================================
# DICAS GENÉRICAS
# ============================================================

define DICAS_GENERICAS_FASE_1 = [

    "Nosso objetivo é chegar à Ilha do Tesouro. Antes de escolher, observe no mapa para onde cada rota pode nos levar.",

    "As letras A e B representam as rotas disponíveis. Observe o resultado de cada escolha antes de continuar.",

    "Se uma rota nos fizer voltar a uma ilha já visitada, ainda podemos escolher um caminho diferente na próxima passagem.",
]


# ============================================================
# DICAS INTERMEDIÁRIAS
# ============================================================

define DICAS_INTERMEDIARIAS_FASE_1 = [

    "Da Ilha 1, tanto a rota A quanto a rota B levam à Ilha 2.",

    "Na Ilha 2, uma das rotas retorna à Ilha 1 e a outra segue diretamente para o nosso objetivo.",

    "Se voltarmos à Ilha 1, observe novamente as rotas da Ilha 2 quando chegarmos até ela.",
]


# ============================================================
# DICAS ESPECÍFICAS
# ============================================================

define DICAS_ESPECIFICAS_FASE_1 = [

    "Na Ilha 2, escolha a rota B para chegar à Ilha do Tesouro.",

    "A sequência A, B leva da Ilha 1 até a Ilha do Tesouro.",

    "A sequência B, B também leva da Ilha 1 até a Ilha do Tesouro.",
]


# ============================================================
# INTRODUÇÃO
# ============================================================

label fase_1_introducao:

    navegador "Capitão, este primeiro arquipélago será nosso treinamento."

    navegador "No mapa, cada ilha possui rotas identificadas pelas letras A e B. Ao escolher uma delas, seguiremos para a ilha indicada."

    navegador "Nem toda escolha precisa nos aproximar do destino. Algumas rotas podem até nos fazer voltar."

    navegador "Nosso objetivo é simples: encontrar um caminho até a Ilha do Tesouro."

    return


# ============================================================
# PREPARAÇÃO DA FASE
# ============================================================

label fase_1_preparar:

    # O botão comum de Dica utiliza somente
    # as dicas genéricas da fase.
    #
    # As dicas intermediárias e específicas
    # ficam disponíveis para o sistema fuzzy
    # de assistência do NPC.

    $ dicas_disponiveis = list(
        DICAS_GENERICAS_FASE_1
    )

    return


# ============================================================
# PEDIR DICA NORMAL
# ============================================================

label fase_1_pedir_dica:

    # Cada solicitação é registrada como uma ocorrência
    # da métrica Dicas Pedidas.

    $ dicas_pedidas += 1


    # Atualiza a Necessidade de Assistência
    # após a nova solicitação.

    call atualizar_necessidade_assistencia


    # ========================================================
    # SEM MAIS DICAS
    # ========================================================

    if not dicas_disponiveis:

        navegador "Capitão, já te contei tudo que sabia sobre esses mares!"

        return


    # ========================================================
    # ESCOLHER DICA
    # ========================================================

    $ dica_escolhida = renpy.random.choice(
        dicas_disponiveis
    )


    # Remove a dica para impedir repetição
    # pelo Navegador enquanto houver outras disponíveis.

    $ dicas_disponiveis.remove(
        dica_escolhida
    )


    navegador "[dica_escolhida]"


    return


# ============================================================
# FORNECER DICA DO NPC
# ============================================================

label fase_1_fornecer_dica_npc:


    # ========================================================
    # GENÉRICA
    # ========================================================

    if categoria_assistencia == "generica":

        call fornecer_dica_npc_com_banco(
            DICAS_GENERICAS_FASE_1
        )


    # ========================================================
    # INTERMEDIÁRIA
    # ========================================================

    elif categoria_assistencia == "intermediaria":

        call fornecer_dica_npc_com_banco(
            DICAS_INTERMEDIARIAS_FASE_1
        )


    # ========================================================
    # ESPECÍFICA
    # ========================================================

    elif categoria_assistencia == "especifica":

        call fornecer_dica_npc_com_banco(
            DICAS_ESPECIFICAS_FASE_1
        )


    # ========================================================
    # NENHUMA
    # ========================================================

    else:

        call npc_recusar_dica


    return
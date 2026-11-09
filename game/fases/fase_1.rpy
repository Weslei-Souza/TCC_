# ============================================================
# FASE 1
# TUTORIAL DE NAVEGAÇÃO
# ============================================================


# ============================================================
# DICAS GENÉRICAS
# ============================================================

define DICAS_GENERICAS_FASE_1 = [

    "A Ilha do Tesouro é o nosso destino. Observe as rotas disponíveis antes de escolher.",
]


# ============================================================
# DICAS INTERMEDIÁRIAS
# ============================================================

define DICAS_INTERMEDIARIAS_FASE_1 = [

    "Na Ilha 2, uma das rotas leva de volta à Ilha 1 e a outra segue para o nosso destino.",
]


# ============================================================
# DICAS ESPECÍFICAS
# ============================================================

define DICAS_ESPECIFICAS_FASE_1 = [

    "Quando estiver na Ilha 2, escolha a rota B para chegar à Ilha do Tesouro.",
]


# ============================================================
# INTRODUÇÃO DA FASE
# ============================================================

label fase_1_introducao:

    navegador "Capitão, vamos começar por estas ilhas."

    navegador "Observe para onde cada rota nos leva e tente chegar à Ilha do Tesouro."

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

        navegador "Sem mais dicas pra você!"

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
# ============================================================
# FASE 2
# ============================================================


# ============================================================
# DICAS
# ============================================================

define DICAS_GENERICAS_FASE_2 = [
    "Dica genérica da Fase 2.",
]

define DICAS_INTERMEDIARIAS_FASE_2 = [
    "Dica intermediária da Fase 2.",
]

define DICAS_ESPECIFICAS_FASE_2 = [
    "Dica específica da Fase 2.",
]


# ============================================================
# INTRODUÇÃO
# ============================================================

label fase_2_introducao:

    navegador "Esta fase ainda será configurada."

    return


# ============================================================
# PREPARAÇÃO
# ============================================================

label fase_2_preparar:

    $ dicas_disponiveis = list(
        DICAS_GENERICAS_FASE_2
    )

    return


# ============================================================
# DICA NORMAL
# ============================================================

label fase_2_pedir_dica:

    $ dicas_pedidas += 1

    call atualizar_necessidade_assistencia


    if not dicas_disponiveis:

        navegador "Sem mais dicas pra você!"

        return


    $ dica_escolhida = renpy.random.choice(
        dicas_disponiveis
    )


    $ dicas_disponiveis.remove(
        dica_escolhida
    )


    navegador "[dica_escolhida]"


    return


# ============================================================
# DICA DO NPC
# ============================================================

label fase_2_fornecer_dica_npc:


    if categoria_assistencia == "generica":

        call fornecer_dica_npc_com_banco(
            DICAS_GENERICAS_FASE_2
        )


    elif categoria_assistencia == "intermediaria":

        call fornecer_dica_npc_com_banco(
            DICAS_INTERMEDIARIAS_FASE_2
        )


    elif categoria_assistencia == "especifica":

        call fornecer_dica_npc_com_banco(
            DICAS_ESPECIFICAS_FASE_2
        )


    else:

        call npc_recusar_dica


    return


# ============================================================
# REPRESENTAÇÃO DOS ESTADOS
# ============================================================

label fase_2_exibir_estado:

    "Visual da Fase 2 ainda não configurado."

    return
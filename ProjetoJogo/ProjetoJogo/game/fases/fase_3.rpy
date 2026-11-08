# ============================================================
# FASE 3
# ============================================================


# ============================================================
# DICAS
# ============================================================

define DICAS_GENERICAS_FASE_3 = [
    "Dica genérica da Fase 3.",
]

define DICAS_INTERMEDIARIAS_FASE_3 = [
    "Dica intermediária da Fase 3.",
]

define DICAS_ESPECIFICAS_FASE_3 = [
    "Dica específica da Fase 3.",
]


# ============================================================
# INTRODUÇÃO
# ============================================================

label fase_3_introducao:

    navegador "Esta fase ainda será configurada."

    return


# ============================================================
# PREPARAÇÃO
# ============================================================

label fase_3_preparar:

    $ dicas_disponiveis = list(
        DICAS_GENERICAS_FASE_3
    )

    return


# ============================================================
# DICA NORMAL
# ============================================================

label fase_3_pedir_dica:

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

label fase_3_fornecer_dica_npc:


    if categoria_assistencia == "generica":

        call fornecer_dica_npc_com_banco(
            DICAS_GENERICAS_FASE_3
        )


    elif categoria_assistencia == "intermediaria":

        call fornecer_dica_npc_com_banco(
            DICAS_INTERMEDIARIAS_FASE_3
        )


    elif categoria_assistencia == "especifica":

        call fornecer_dica_npc_com_banco(
            DICAS_ESPECIFICAS_FASE_3
        )


    else:

        call npc_recusar_dica


    return


# ============================================================
# REPRESENTAÇÃO DOS ESTADOS
# ============================================================

label fase_3_exibir_estado:

    "Visual da Fase 3 ainda não configurado."

    return
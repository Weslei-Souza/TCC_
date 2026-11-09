# ============================================================
# FASE 6

# ============================================================
define DICAS_GENERICAS_FASE_6 = [

    "Este arquipélago é mais perigoso. Há mais de uma prisão e vários caminhos possíveis.",

    "Uma rota aparentemente curta pode terminar em uma armadilha.",
]


define DICAS_INTERMEDIARIAS_FASE_6 = [

    "A Ilha 4 possui uma rota que leva a uma prisão.",

    "A Ilha 5 também possui uma rota perigosa que termina em uma prisão.",

    "Na Ilha 7, apenas uma das rotas leva à Ilha do Tesouro.",
]


define DICAS_ESPECIFICAS_FASE_6 = [

    "A sequência A, B, B, A, B leva até a Ilha do Tesouro.",

    "Na Ilha 7, escolha B. A rota A leva a uma prisão.",
]

label fase_6_introducao:

    navegador "Capitão, estas águas estão ficando perigosas."

    navegador "Há duas prisões e vários caminhos que podem nos afastar do destino."

    return
# ============================================================
# PREPARAÇÃO
# ============================================================

label fase_6_preparar:

    $ dicas_disponiveis = list(
        DICAS_GENERICAS_FASE_6

    )

    return


# ============================================================
# DICA NORMAL
# ============================================================

label fase_6_pedir_dica:

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

label fase_6_fornecer_dica_npc:


    if categoria_assistencia == "generica":

        call fornecer_dica_npc_com_banco(
            DICAS_GENERICAS_FASE_6

        )


    elif categoria_assistencia == "intermediaria":

        call fornecer_dica_npc_com_banco(
            DICAS_INTERMEDIARIAS_FASE_6

        )


    elif categoria_assistencia == "especifica":

        call fornecer_dica_npc_com_banco(
            DICAS_ESPECIFICAS_FASE_6

        )


    else:

        call npc_recusar_dica


    return


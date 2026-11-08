define DICAS_GENERICAS_FASE_5 = [

    "Agora teremos que lidar ao mesmo tempo com caminhos alternativos, redemoinhos e a prisão.",

    "Observe o mapa antes de escolher: algumas regiões possuem mais de um perigo.",
]

define DICAS_INTERMEDIARIAS_FASE_5 = [

    "A Ilha 4 possui um redemoinho na rota A.",

    "Tanto a Ilha 5 quanto a Ilha 6 possuem uma rota que leva à prisão.",
]

define DICAS_ESPECIFICAS_FASE_5 = [

    "A sequência A, A, B, B leva até a Ilha Final.",

    "Na Ilha 6, escolha B. A rota A leva à prisão.",
]

label fase_5_introducao:

    navegador "Capitão, desta vez teremos que usar tudo que vimos até agora."

    navegador "Há diferentes caminhos, redemoinhos e uma prisão nestas águas."

    return


# ============================================================
# PREPARAÇÃO
# ============================================================

label fase_5_preparar:

    $ dicas_disponiveis = list(
        DICAS_GENERICAS_FASE_5
    )

    return


# ============================================================
# DICA NORMAL
# ============================================================

label fase_5_pedir_dica:

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

label fase_5_fornecer_dica_npc:


    if categoria_assistencia == "generica":

        call fornecer_dica_npc_com_banco(
            DICAS_GENERICAS_FASE_5
        )


    elif categoria_assistencia == "intermediaria":

        call fornecer_dica_npc_com_banco(
            DICAS_INTERMEDIARIAS_FASE_5
        )


    elif categoria_assistencia == "especifica":

        call fornecer_dica_npc_com_banco(
            DICAS_ESPECIFICAS_FASE_5
        )


    else:

        call npc_recusar_dica


    return


# ============================================================
# REPRESENTAÇÃO DOS ESTADOS
# ============================================================

label fase_5_exibir_estado:

    "Visual da Fase 5 ainda não configurado."

    return
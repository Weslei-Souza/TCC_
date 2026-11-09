# ============================================================
# FASE 7
# ============================================================
define DICAS_GENERICAS_FASE_7 = [

    "Este é o arquipélago mais complexo que encontramos até agora.",

    "Há redemoinhos, retornos e duas prisões espalhadas pelas rotas.",
]


define DICAS_INTERMEDIARIAS_FASE_7 = [

    "As Ilhas 3, 6 e 8 possuem redemoinhos.",

    "As Ilhas 2 e 4 possuem rotas que levam a uma prisão.",

    "As Ilhas 7 e 9 também possuem rotas que terminam em uma prisão.",
]


define DICAS_ESPECIFICAS_FASE_7 = [

    "Uma rota possível até o objetivo começa com A, A.",

    "A sequência A, A, B, A, B, B leva até a Ilha do Tesouro.",

    "Na Ilha 9, escolha B. A rota A leva a uma prisão.",
]
label fase_7_introducao:

    navegador "Capitão, chegamos ao arquipélago mais perigoso da viagem."

    navegador "Vamos precisar observar o mapa e planejar cada rota com cuidado."

    return

# ============================================================
# PREPARAÇÃO
# ============================================================

label fase_7_preparar:

    $ dicas_disponiveis = list(
        DICAS_GENERICAS_FASE_7
    )

    return


# ============================================================
# DICA NORMAL
# ============================================================

label fase_7_pedir_dica:

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

label fase_7_fornecer_dica_npc:


    if categoria_assistencia == "generica":

        call fornecer_dica_npc_com_banco(
            DICAS_GENERICAS_FASE_7
        )


    elif categoria_assistencia == "intermediaria":

        call fornecer_dica_npc_com_banco(
            DICAS_INTERMEDIARIAS_FASE_7
        )


    elif categoria_assistencia == "especifica":

        call fornecer_dica_npc_com_banco(
            DICAS_ESPECIFICAS_FASE_7
        )


    else:

        call npc_recusar_dica


    return


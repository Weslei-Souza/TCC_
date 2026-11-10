# ============================================================
# FASE 6

# ============================================================
define DICAS_GENERICAS_FASE_6 = [

    "Este arquipélago possui duas prisões e diferentes regiões perigosas. Uma sequência curta nem sempre é uma sequência segura.",

    "Procure identificar primeiro quais escolhas levam diretamente às prisões. Eliminá-las pode facilitar o planejamento.",

    "O mapa possui retornos e um redemoinho. Planejar alguns movimentos à frente será mais seguro do que escolher apenas pela proximidade do destino.",
]


define DICAS_INTERMEDIARIAS_FASE_6 = [

    "Na Ilha 2, a rota A entra no redemoinho. A rota B permite avançar para a Ilha 4.",

    "Na Ilha 4, a rota A leva a uma prisão; na Ilha 5, a rota B também leva a uma prisão.",

    "Depois da Ilha 6 ainda há perigo: na Ilha 7, somente uma das rotas alcança a Ilha do Tesouro.",
]


define DICAS_ESPECIFICAS_FASE_6 = [

    "A sequência A, B, B, A, B leva da Ilha 1 até a Ilha do Tesouro.",

    "Outra sequência válida é B, A, A, A, B.",

    "Se estiver na Ilha 4, escolha B; depois, na Ilha 6, escolha A; e na Ilha 7, escolha B.",
]


label fase_6_introducao:

    navegador "Capitão, agora entramos em águas realmente perigosas."

    navegador "Há duas prisões espalhadas pelo arquipélago, além de retornos e um redemoinho."

    navegador "Algumas rotas chegam perto do nosso destino, mas uma única escolha errada pode encerrar toda a tentativa."

    navegador "Observe os caminhos com atenção e tente planejar uma sequência segura até a Ilha do Tesouro."

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

        navegador "Capitão, já te contei tudo que sabia sobre esses mares!"

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


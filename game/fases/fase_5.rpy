


define DICAS_GENERICAS_FASE_5 = [

    "A partir daqui não há um elemento novo para descobrir. O desafio é combinar tudo o que já encontramos.",

    "Caminhos alternativos, retornos, redemoinhos e prisão aparecem juntos neste arquipélago.",

    "Antes de executar uma sequência longa, procure no mapa quais ilhas oferecem rotas seguras para continuar avançando.",
]


define DICAS_INTERMEDIARIAS_FASE_5 = [

    "Na Ilha 4, a rota A entra no redemoinho e nos mantém na mesma ilha.",

    "Na Ilha 5, a rota A leva à prisão, enquanto B permite continuar.",

    "Na Ilha 6, apenas a rota B leva à Ilha do Tesouro. A outra termina na prisão.",
]


define DICAS_ESPECIFICAS_FASE_5 = [

    "A sequência A, A, B, B leva da Ilha 1 até a Ilha do Tesouro.",

    "A sequência A, B, B, B também leva ao objetivo.",

    "Outra sequência possível é B, A, B, B.",
]


label fase_5_introducao:

    navegador "Capitão, já conhecemos todos os perigos básicos destas águas."

    navegador "Desta vez eles aparecem juntos: caminhos que retornam, redemoinhos e uma prisão fazem parte do mesmo arquipélago."

    navegador "Não basta apenas seguir em frente. Algumas escolhas aparentemente boas podem nos levar a uma armadilha."

    navegador "Considere esta nossa primeira navegação completa: observe o mapa, planeje a rota e encontre a Ilha do Tesouro."

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


# ============================================================
# FASE 2
# CAMINHOS ALTERNATIVOS
# ============================================================
define DICAS_GENERICAS_FASE_2 = [

    "Este arquipélago possui diferentes caminhos até a Ilha do Tesouro. Não existe apenas uma sequência possível.",

    "Uma rota que nos leva para longe do destino pode fazer parte de um caminho válido mais adiante.",

    "Observe como as ilhas se conectam. Pensar em algumas escolhas à frente pode evitar voltas desnecessárias.",
]


define DICAS_INTERMEDIARIAS_FASE_2 = [

    "Na Ilha 3, a rota A segue para a Ilha 5, enquanto a rota B retorna à Ilha 1.",

    "Na Ilha 4, a rota B segue para a Ilha 5, mas a rota A nos devolve à Ilha 1.",

    "A Ilha 5 está muito próxima do objetivo: uma de suas rotas leva diretamente à Ilha do Tesouro.",
]


define DICAS_ESPECIFICAS_FASE_2 = [

    "A sequência B, A, B leva da Ilha 1 até a Ilha do Tesouro.",

    "Outra sequência possível é A, A, A, B.",

    "A sequência A, B, B, B também encontra a Ilha do Tesouro.",
]


label fase_2_introducao:

    navegador "Capitão, a partir daqui as águas começam a oferecer mais possibilidades."

    navegador "Este arquipélago possui vários caminhos entre as ilhas. Rotas diferentes podem acabar nos levando ao mesmo destino."

    navegador "Também podemos encontrar caminhos que retornam a lugares por onde já passamos."

    navegador "Antes de navegar, observe o mapa e tente identificar mais de uma forma de chegar à Ilha do Tesouro."

    return



label fase_2_preparar:

    $ dicas_disponiveis = list(
        DICAS_GENERICAS_FASE_2
    )

    return


label fase_2_pedir_dica:

    $ dicas_pedidas += 1

    call atualizar_necessidade_assistencia from _call_atualizar_necessidade_assistencia_4


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


label fase_2_fornecer_dica_npc:

    if categoria_assistencia == "generica":

        call fornecer_dica_npc_com_banco(
            DICAS_GENERICAS_FASE_2
        ) from _call_fornecer_dica_npc_com_banco_3

    elif categoria_assistencia == "intermediaria":

        call fornecer_dica_npc_com_banco(
            DICAS_INTERMEDIARIAS_FASE_2
        ) from _call_fornecer_dica_npc_com_banco_4

    elif categoria_assistencia == "especifica":

        call fornecer_dica_npc_com_banco(
            DICAS_ESPECIFICAS_FASE_2
        ) from _call_fornecer_dica_npc_com_banco_5

    else:

        call npc_recusar_dica from _call_npc_recusar_dica_2

    return

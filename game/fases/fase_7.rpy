# ============================================================
# FASE 7
# ============================================================


define DICAS_GENERICAS_FASE_7 = [

    "Este é o maior arquipélago da viagem. Há vários caminhos, três redemoinhos e duas prisões entre nós e o tesouro.",

    "Não tente decidir apenas pela ilha que parece mais próxima do objetivo. Algumas rotas avançam visualmente, mas terminam em armadilhas.",

    "Divida o problema em partes: encontre primeiro uma região segura do mapa e, a partir dela, planeje o trecho seguinte.",
]


define DICAS_INTERMEDIARIAS_FASE_7 = [

    "As Ilhas 3, 6 e 8 possuem redemoinhos. Observe quais letras ativam cada um deles.",

    "Na Ilha 2, a rota B leva a uma prisão; na Ilha 4, a rota A também termina em uma prisão.",

    "Na parte final do percurso, a Ilha 7 possui uma rota para a prisão e a Ilha 9 também. Chegar perto do tesouro ainda não garante segurança.",
]


define DICAS_ESPECIFICAS_FASE_7 = [

    "A sequência A, A, B, A, B, B leva da Ilha 1 até a Ilha do Tesouro.",

    "Também existe uma rota que começa por B, B e pode chegar ao objetivo com a sequência B, B, A, A, A, B, B.",

    "Se estiver na Ilha 2, uma sequência segura até o tesouro é A, B, A, B, B.",
]




label fase_7_introducao:

    navegador "Capitão, chegamos ao último arquipélago da nossa viagem."

    navegador "Aqui tudo o que encontramos antes aparece ao mesmo tempo: caminhos alternativos, retornos, três redemoinhos e duas prisões."

    navegador "O caminho até a Ilha do Tesouro é mais longo e algumas rotas perigosas aparecem mesmo quando já estamos próximos do objetivo."

    navegador "Este é o desafio final. Observe todo o mapa, planeje com cuidado e escolha nossa rota."

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


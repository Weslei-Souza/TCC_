# ============================================================
# FASE 7
# ============================================================

define DICAS_GENERICAS_FASE_7 = [

    "Este é o arquipélago mais complexo que encontramos até agora.",

    "Há redemoinhos, retornos e duas prisões espalhadas pelas rotas.",
]

define DICAS_INTERMEDIARIAS_FASE_7 = [

    "As Ilhas 3, 6 e 8 possuem redemoinhos.",

    "A Ilha 2 e a Ilha 4 possuem caminhos que levam à Prisão 1.",

    "A Ilha 7 e a Ilha 9 possuem caminhos que levam à Prisão 2.",
]

define DICAS_ESPECIFICAS_FASE_7 = [

    "Uma rota possível até o objetivo começa com A, A.",

    "A sequência A, A, B, A, B, B leva até a Ilha do Tesouro.",

    "Na Ilha 9, escolha B. A rota A leva à Prisão 2.",
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


# ============================================================
# REPRESENTAÇÃO DOS ESTADOS
# ============================================================

label fase_7_exibir_estado:

    scene bg_mar

    $ nome_estado_fase = automato.nome_estado(
        configuracao_automato,
        estado_atual
    )

    if automato.eh_armadilha(
        configuracao_automato,
        estado_atual
    ):

        "Você chegou à [nome_estado_fase]."

    elif automato.eh_final(
        configuracao_automato,
        estado_atual
    ):

        "Você chegou à [nome_estado_fase]."

    else:

        "Você está em [nome_estado_fase]."

    return
# ============================================================
# FASE 3
# REDEMOINHOS / AUTO-LAÇOS
# ============================================================


define DICAS_GENERICAS_FASE_3 = [

    "Existem redemoinhos nestas águas. Algumas rotas podem nos deixar exatamente onde já estávamos.",

    "Se uma escolha não mudar nossa posição, talvez tenhamos encontrado um redemoinho.",
]


define DICAS_INTERMEDIARIAS_FASE_3 = [

    "Na Ilha 2, a rota A nos mantém na própria Ilha 2.",

    "A Ilha 5 possui uma rota para a Ilha do Tesouro, mas outra nos leva de volta ao início.",
]


define DICAS_ESPECIFICAS_FASE_3 = [

    "A sequência A, B, A, B leva da Ilha 1 até a Ilha do Tesouro.",

    "Ao chegar à Ilha 5, escolha B para alcançar a Ilha do Tesouro.",
]


label fase_3_introducao:

    navegador "Capitão, parece que estas águas possuem redemoinhos."

    navegador "Algumas rotas podem acabar nos levando para o mesmo lugar de onde saímos."

    return


label fase_3_preparar:

    $ dicas_disponiveis = list(
        DICAS_GENERICAS_FASE_3
    )

    return


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


label fase_3_exibir_estado:

    scene bg_mar

    $ nome_estado_fase = automato.nome_estado(
        configuracao_automato,
        estado_atual
    )

    if automato.eh_final(
        configuracao_automato,
        estado_atual
    ):

        "Você chegou à [nome_estado_fase]."

    else:

        "Você está em [nome_estado_fase]."

    return
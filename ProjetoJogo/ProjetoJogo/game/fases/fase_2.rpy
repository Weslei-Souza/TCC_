# ============================================================
# FASE 2
# CAMINHOS ALTERNATIVOS
# ============================================================


define DICAS_GENERICAS_FASE_2 = [

    "Este arquipélago possui mais de um caminho até o destino.",

    "Nem toda rota que nos afasta da Ilha Final significa que estamos perdidos.",
]


define DICAS_INTERMEDIARIAS_FASE_2 = [

    "A Ilha 5 possui uma rota que leva diretamente à Ilha Final.",

    "Algumas rotas podem nos levar de volta à Ilha 1.",
]


define DICAS_ESPECIFICAS_FASE_2 = [

    "Partindo da Ilha 1, a sequência B, A, B leva até a Ilha Final.",

    "Da Ilha 3, a rota A leva à Ilha 5; de lá, B chega à Ilha Final.",
]


label fase_2_introducao:

    navegador "Capitão, este arquipélago parece ter mais de um caminho possível."

    navegador "Vamos observar as rotas antes de decidir por onde seguir."

    return


label fase_2_preparar:

    $ dicas_disponiveis = list(
        DICAS_GENERICAS_FASE_2
    )

    return


label fase_2_pedir_dica:

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


label fase_2_fornecer_dica_npc:

    if categoria_assistencia == "generica":

        call fornecer_dica_npc_com_banco(
            DICAS_GENERICAS_FASE_2
        )

    elif categoria_assistencia == "intermediaria":

        call fornecer_dica_npc_com_banco(
            DICAS_INTERMEDIARIAS_FASE_2
        )

    elif categoria_assistencia == "especifica":

        call fornecer_dica_npc_com_banco(
            DICAS_ESPECIFICAS_FASE_2
        )

    else:

        call npc_recusar_dica

    return


label fase_2_exibir_estado:

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
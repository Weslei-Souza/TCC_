# ============================================================
# FASE 4
# PRISÃO / ESTADO DE MORTE
# ============================================================


define DICAS_GENERICAS_FASE_4 = [

    "Há uma prisão entre estas ilhas. Precisamos evitar as rotas que levam até ela.",

    "Nem toda rota disponível é segura.",
]


define DICAS_INTERMEDIARIAS_FASE_4 = [

    "A Ilha 4 possui uma rota perigosa que leva diretamente à prisão.",

    "A Ilha 6 está próxima do objetivo, mas uma das escolhas ainda leva à prisão.",
]


define DICAS_ESPECIFICAS_FASE_4 = [

    "A sequência B, B, A, B leva até a Ilha Final.",

    "Na Ilha 6, escolha B. A rota A leva à prisão.",
]


label fase_4_introducao:

    navegador "Capitão, avistamos uma prisão entre estas ilhas."

    navegador "Se formos parar lá, estaremos presos e nossa viagem termina."

    return


label fase_4_preparar:

    $ dicas_disponiveis = list(
        DICAS_GENERICAS_FASE_4
    )

    return


label fase_4_pedir_dica:

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


label fase_4_fornecer_dica_npc:

    if categoria_assistencia == "generica":

        call fornecer_dica_npc_com_banco(
            DICAS_GENERICAS_FASE_4
        )

    elif categoria_assistencia == "intermediaria":

        call fornecer_dica_npc_com_banco(
            DICAS_INTERMEDIARIAS_FASE_4
        )

    elif categoria_assistencia == "especifica":

        call fornecer_dica_npc_com_banco(
            DICAS_ESPECIFICAS_FASE_4
        )

    else:

        call npc_recusar_dica

    return


label fase_4_exibir_estado:

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
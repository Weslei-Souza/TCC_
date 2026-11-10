# ============================================================
# FASE 3
# REDEMOINHOS / AUTO-LAÇOS
# ============================================================



define DICAS_GENERICAS_FASE_3 = [

    "Há redemoinhos nestas águas. Algumas escolhas podem nos fazer permanecer exatamente na mesma ilha.",

    "Se navegarmos e acabarmos no mesmo lugar, observe qual rota provocou isso antes de tentar novamente.",

    "Um redemoinho não significa que estamos presos para sempre. Outra rota da mesma ilha ainda pode nos permitir continuar.",
]


define DICAS_INTERMEDIARIAS_FASE_3 = [

    "Na Ilha 2, a rota A nos mantém na própria Ilha 2. A rota B permite seguir viagem.",

    "Na Ilha 4, uma rota segue para a Ilha 5 e a outra retorna à Ilha 2.",

    "Na Ilha 5, uma escolha nos leva de volta ao início e a outra segue para a Ilha do Tesouro.",
]


define DICAS_ESPECIFICAS_FASE_3 = [

    "A sequência A, B, A, B leva da Ilha 1 até a Ilha do Tesouro.",

    "Outra rota possível é B, A, A, B.",

    "Se estiver na Ilha 2, a sequência B, A, B leva até a Ilha do Tesouro.",
]


label fase_3_introducao:

    navegador "Capitão, há algo diferente nestas águas."

    navegador "Algumas rotas passam por redemoinhos. Se entrarmos em um deles, podemos terminar exatamente na mesma ilha de onde tentamos sair."

    navegador "Isso não encerra nossa viagem, mas repetir a mesma escolha pode nos manter presos naquele ponto."

    navegador "Observe os redemoinhos no mapa e procure uma rota que continue avançando até a Ilha do Tesouro."

    return



label fase_3_preparar:

    $ dicas_disponiveis = list(
        DICAS_GENERICAS_FASE_3
    )

    return


label fase_3_pedir_dica:

    $ dicas_pedidas += 1

    call atualizar_necessidade_assistencia from _call_atualizar_necessidade_assistencia_5


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


label fase_3_fornecer_dica_npc:

    if categoria_assistencia == "generica":

        call fornecer_dica_npc_com_banco(
            DICAS_GENERICAS_FASE_3
        ) from _call_fornecer_dica_npc_com_banco_6

    elif categoria_assistencia == "intermediaria":

        call fornecer_dica_npc_com_banco(
            DICAS_INTERMEDIARIAS_FASE_3
        ) from _call_fornecer_dica_npc_com_banco_7

    elif categoria_assistencia == "especifica":

        call fornecer_dica_npc_com_banco(
            DICAS_ESPECIFICAS_FASE_3
        ) from _call_fornecer_dica_npc_com_banco_8

    else:

        call npc_recusar_dica from _call_npc_recusar_dica_3

    return


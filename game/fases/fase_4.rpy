# ============================================================
# FASE 4
# PRISÃO / ESTADO DE MORTE
# ============================================================

define DICAS_GENERICAS_FASE_4 = [

    "Agora há uma prisão no arquipélago. Precisamos considerar não apenas como avançar, mas também quais rotas evitar.",

    "Ao contrário de um redemoinho, entrar na prisão encerra nossa tentativa.",

    "Uma rota aparentemente mais direta pode ser perigosa. Observe o destino de cada escolha antes de navegar.",
]


define DICAS_INTERMEDIARIAS_FASE_4 = [

    "A Ilha 3 possui um redemoinho na rota A. A outra rota permite continuar viagem.",

    "Na Ilha 4, a rota A leva diretamente à prisão.",

    "Na Ilha 6, uma rota leva à prisão e a outra alcança a Ilha do Tesouro.",
]


define DICAS_ESPECIFICAS_FASE_4 = [

    "A sequência B, B, A, B leva da Ilha 1 até a Ilha do Tesouro.",

    "Uma rota alternativa segura começa com A, B, B.",

    "Quando chegar à Ilha 6, escolha B. A rota A termina na prisão.",
]


label fase_4_introducao:

    navegador "Capitão, este arquipélago apresenta um perigo novo."

    navegador "Há uma prisão entre as rotas. Se nosso navio for levado até ela, não teremos uma rota de fuga e a tentativa termina."

    navegador "Os redemoinhos continuam presentes, mas agora precisamos distinguir um atraso de um caminho realmente sem saída."

    navegador "Use o mapa com cuidado e procure chegar à Ilha do Tesouro sem passar pela prisão."

    return

label fase_4_preparar:

    $ dicas_disponiveis = list(
        DICAS_GENERICAS_FASE_4
    )

    return


label fase_4_pedir_dica:

    $ dicas_pedidas += 1

    call atualizar_necessidade_assistencia from _call_atualizar_necessidade_assistencia_6


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


label fase_4_fornecer_dica_npc:

    if categoria_assistencia == "generica":

        call fornecer_dica_npc_com_banco(
            DICAS_GENERICAS_FASE_4
        ) from _call_fornecer_dica_npc_com_banco_9

    elif categoria_assistencia == "intermediaria":

        call fornecer_dica_npc_com_banco(
            DICAS_INTERMEDIARIAS_FASE_4
        ) from _call_fornecer_dica_npc_com_banco_10

    elif categoria_assistencia == "especifica":

        call fornecer_dica_npc_com_banco(
            DICAS_ESPECIFICAS_FASE_4
        ) from _call_fornecer_dica_npc_com_banco_11

    else:

        call npc_recusar_dica from _call_npc_recusar_dica_4

    return


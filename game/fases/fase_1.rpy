# ============================================================
# FASE 1
# TUTORIAL DE NAVEGAÇÃO
# ============================================================


# ============================================================
# DICAS GENÉRICAS
# ============================================================

define DICAS_GENERICAS_FASE_1 = [

    "A Ilha do Tesouro é o nosso destino. Observe as rotas disponíveis antes de escolher.",
]


# ============================================================
# DICAS INTERMEDIÁRIAS
# ============================================================

define DICAS_INTERMEDIARIAS_FASE_1 = [

    "Na Ilha 2, uma das rotas leva de volta à Ilha 1 e a outra segue para o nosso destino.",
]


# ============================================================
# DICAS ESPECÍFICAS
# ============================================================

define DICAS_ESPECIFICAS_FASE_1 = [

    "Quando estiver na Ilha 2, escolha a rota B para chegar à Ilha do Tesouro.",
]


# ============================================================
# INTRODUÇÃO DA FASE
# ============================================================

label fase_1_introducao:

    navegador "Capitão, vamos começar por estas ilhas."

    navegador "Observe para onde cada rota nos leva e tente chegar à Ilha do Tesouro."

    return


# ============================================================
# PREPARAÇÃO DA FASE
# ============================================================

label fase_1_preparar:

    # O botão comum de Dica utiliza somente
    # as dicas genéricas da fase.
    #
    # As dicas intermediárias e específicas
    # ficam disponíveis para o sistema fuzzy
    # de assistência do NPC.

    $ dicas_disponiveis = list(
        DICAS_GENERICAS_FASE_1
    )

    return


# ============================================================
# PEDIR DICA NORMAL
# ============================================================

label fase_1_pedir_dica:

    # Cada solicitação é registrada como uma ocorrência
    # da métrica Dicas Pedidas.

    $ dicas_pedidas += 1


    # Atualiza a Necessidade de Assistência
    # após a nova solicitação.

    call atualizar_necessidade_assistencia


    # ========================================================
    # SEM MAIS DICAS
    # ========================================================

    if not dicas_disponiveis:

        navegador "Sem mais dicas pra você!"

        return


    # ========================================================
    # ESCOLHER DICA
    # ========================================================

    $ dica_escolhida = renpy.random.choice(
        dicas_disponiveis
    )


    # Remove a dica para impedir repetição
    # pelo Navegador enquanto houver outras disponíveis.

    $ dicas_disponiveis.remove(
        dica_escolhida
    )


    navegador "[dica_escolhida]"


    return


# ============================================================
# REPRESENTAÇÃO DOS ESTADOS
# ============================================================

label fase_1_exibir_estado:


    # ========================================================
    # q0 - ILHA 1 / ESTADO INICIAL
    # ========================================================

    if estado_atual == "q0":

        scene bg_ilha1_fase1

        "Você está na Ilha 1."


    # ========================================================
    # q1 - ILHA 2
    # ========================================================

    elif estado_atual == "q1":

        scene bg_ilha2_fase1

        "Você está na Ilha 2."


    # ========================================================
    # qf - Ilha do Tesouro
    # ========================================================

    elif estado_atual == "qf":

        scene bg_final_fase1

        "Você chegou à Ilha do Tesouro."


    return


# ============================================================
# MAPA DA FASE 1
# ============================================================

# Este mapa ainda utiliza a interface provisória.
#
# Posteriormente será substituído por uma imagem
# definitiva baseada no autômato modelado no JFLAP.

screen mapa_fase_1:

    add "mapa_fundo"


    frame:

        background Solid("#111820CC")

        xalign 0.5
        yalign 0.5

        xsize 1100
        ysize 650


        fixed:


            # =================================================
            # ILHA 1 - q0
            # =================================================

            add Transform(
                "bg_ilha1_fase1",
                xysize=(220, 140),
                fit="contain"
            ):

                xpos 80
                ypos 250


            text "Ilha 1":

                xpos 140
                ypos 400


            # =================================================
            # ILHA 2 - q1
            # =================================================

            add Transform(
                "bg_ilha2_fase1",
                xysize=(220, 140),
                fit="contain"
            ):

                xpos 430
                ypos 250


            text "Ilha 2":

                xpos 490
                ypos 400


            # =================================================
            # Ilha do Tesouro - qf
            # =================================================

            add Transform(
                "bg_final_fase1",
                xysize=(220, 140),
                fit="contain"
            ):

                xpos 790
                ypos 250


            text "Ilha do Tesouro":

                xpos 835
                ypos 400


            # =================================================
            # INDICAÇÕES PROVISÓRIAS DAS ROTAS
            # =================================================

            # q0 -> q1
            text "A / B":

                xpos 350
                ypos 235

                size 28


            # q1 -> q0
            text "A ←":

                xpos 350
                ypos 350

                size 28


            # q1 -> qf
            text "B →":

                xpos 700
                ypos 270

                size 28


            # =================================================
            # FECHAR
            # =================================================

            textbutton "Fechar mapa":

                style "rota_button"

                xpos 820
                ypos 520

                action Hide("mapa_atual")


# ============================================================
# FORNECER DICA DO NPC
# ============================================================

label fase_1_fornecer_dica_npc:


    # ========================================================
    # GENÉRICA
    # ========================================================

    if categoria_assistencia == "generica":

        call fornecer_dica_npc_com_banco(
            DICAS_GENERICAS_FASE_1
        )


    # ========================================================
    # INTERMEDIÁRIA
    # ========================================================

    elif categoria_assistencia == "intermediaria":

        call fornecer_dica_npc_com_banco(
            DICAS_INTERMEDIARIAS_FASE_1
        )


    # ========================================================
    # ESPECÍFICA
    # ========================================================

    elif categoria_assistencia == "especifica":

        call fornecer_dica_npc_com_banco(
            DICAS_ESPECIFICAS_FASE_1
        )


    # ========================================================
    # NENHUMA
    # ========================================================

    else:

        call npc_recusar_dica


    return
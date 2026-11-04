# ============================================================
# FASE 1
# PRIMEIROS ESTADOS
# ============================================================


# ============================================================
# DICAS DA FASE 1
# ============================================================

# ============================================================
# DICAS GENÉRICAS
# ============================================================

define DICAS_GENERICAS_FASE_1 = [

    "A Ilha 1 é o ponto de partida e a Ilha Final é o seu destino.",
]

# ============================================================
# DICAS INTERMEDIÁRIAS
# ============================================================

define DICAS_INTERMEDIARIAS_FASE_1 = [

    "A Ilha 3 está próxima do objetivo final desta fase.",
]


# ============================================================
# DICAS ESPECÍFICAS
# ============================================================

define DICAS_ESPECIFICAS_FASE_1 = [

    "Você não precisa passar pela Ilha 2 para chegar à Ilha Final, mas pode ser necessário dependendo da rota escolhida.",
]

# ============================================================
# PREPARAÇÃO DA FASE 1
# ============================================================

label fase_1_preparar:

    # Cria uma nova lista aqui para esta partida.

    $ dicas_disponiveis = (
        list(DICAS_GENERICAS_FASE_1)
        + list(DICAS_INTERMEDIARIAS_FASE_1)
        + list(DICAS_ESPECIFICAS_FASE_1)
    )

    $ ultima_dica = None


    return

# ============================================================
# PEDIR DICA - FASE 1
# ============================================================

label fase_1_pedir_dica:

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

# REPRESENTAÇÃO DOS ESTADOS
label fase_1_exibir_estado:

    # --------------------------------------------------------
    # q0 - ESTADO INICIAL
    # --------------------------------------------------------

    if estado_atual == "q0":

        scene bg_ilha1_fase1

        "Você está na Ilha 1."




    # --------------------------------------------------------
    # q1
    # --------------------------------------------------------

    elif estado_atual == "q1":

        scene bg_ilha2_fase1

        "Você está na Ilha 2."



    # --------------------------------------------------------
    # q2
    # --------------------------------------------------------
    elif estado_atual == "q2":

        scene bg_ilha3_fase1

        "Você está na Ilha 3."



    # --------------------------------------------------------
    # qf - ESTADO FINAL
    # --------------------------------------------------------

    elif estado_atual == "qf":

        scene bg_final_fase1

        "Você chegou à Ilha Final."



    return



# ============================================================
# MAPA FASE 1
# ============================================================

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
            # q0
            # =================================================

            add Transform(
                "bg_ilha1_fase1",
                xysize=(220, 140),
                fit="contain"
            ):

                xpos 70
                ypos 250


            text "Ilha 1\n Inicial":

                xpos 90
                ypos 400


            # =================================================
            # q1
            # =================================================

            add Transform(
                "bg_ilha2_fase1",
                xysize=(220, 140),
                fit="contain"
            ):

                xpos 350
                ypos 50


            text "Ilha 2":

                xpos 400
                ypos 200


            # =================================================
            # q2
            # =================================================

            add Transform(
                "bg_ilha3_fase1",
                xysize=(220, 140),
                fit="contain"
            ):

                xpos 350
                ypos 400


            text "Ilha 3":

                xpos 400
                ypos 550


            # =================================================
            # qf
            # =================================================

            add Transform(
                "bg_final_fase1",
                xysize=(220, 140),
                fit="contain"
            ):

                xpos 750
                ypos 225


            text "Ilha Final - Final":

                xpos 780
                ypos 375


            # =================================================
            # TRANSIÇÕES
            # =================================================

            text "A":

                xpos 290
                ypos 175

                size 32


            text "B":

                xpos 290
                ypos 420

                size 32


            text "B":

                xpos 650
                ypos 250

                size 32


            # =================================================
            # FECHAR
            # =================================================

            textbutton "Fechar mapa":

                style "rota_button"

                xpos 720
                ypos 500

                action Hide("mapa_atual")
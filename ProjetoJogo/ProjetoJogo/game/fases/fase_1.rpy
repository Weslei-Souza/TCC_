# ============================================================
# FASE 1
# PRIMEIROS ESTADOS
# ============================================================


# REPRESENTAÇÃO DOS ESTADOS
label fase_1_exibir_estado:

    # --------------------------------------------------------
    # q0 - ESTADO INICIAL
    # --------------------------------------------------------

    if estado_atual == "q0":

        scene bg_ilha1_fase1

        "Você está na Ilha 1."

        "Estado atual: q0."



    # --------------------------------------------------------
    # q1
    # --------------------------------------------------------

    elif estado_atual == "q1":

        scene bg_ilha2_fase1

        "Você está na Ilha 2."

        "Estado atual: q1."


    # --------------------------------------------------------
    # q2
    # --------------------------------------------------------
    elif estado_atual == "q2":

        scene bg_ilha3_fase1

        "Você está na Ilha 3."

        "Estado atual: q2."


    # --------------------------------------------------------
    # qf - ESTADO FINAL
    # --------------------------------------------------------

    elif estado_atual == "qf":

        scene bg_final_fase1

        "Você chegou à Ilha Final."

        "Estado atual: qf."


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


            text "Ilha 1\nq0 - Inicial":

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


            text "Ilha 2\nq1":

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


            text "Ilha 3\nq2":

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


            text "Ilha Final\nqf - Final":

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
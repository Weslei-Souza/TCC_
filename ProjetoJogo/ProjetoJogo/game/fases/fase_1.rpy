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
# CONTROLE DO ENCONTRO DA FASE 1
# ============================================================

# A Fase 1 possui um encontro obrigatório com NPC.
# Ele acontece apenas uma vez durante a execução da fase.

default encontro_npc_fase1_realizado = False

# ============================================================
# PREPARAÇÃO DA FASE 1
# ============================================================

label fase_1_preparar:

    # O botão Dica utiliza somente ad dica genéricas da fase.
    #
    # As dicas intermediárias e específicas ficam 
    # para o sistema de assistência do NPC.
    
    $ dicas_disponiveis = list(
        DICAS_GENERICAS_FASE_1
    )
    #O encontro tutorial do npc ainda não aconteceu
    $ encontro_npc_fase1_realizado = False

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

        # ========================================================
        # ENCONTRO TUTORIAL COM NPC
        # ========================================================

        if not encontro_npc_fase1_realizado:

            call fase_1_encontro_npc


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

# ============================================================
# ENCONTRO COM NPC - FASE 1
# ============================================================

label fase_1_encontro_npc:

    # Marca imediatamente o encontro como realizado
    # para impedir que ele seja disparado novamente
    # ao revisitar a Ilha 3.

    $ encontro_npc_fase1_realizado = True


    "Há alguém nesta ilha."


    # ========================================================
    # INICIA O SISTEMA GERAL DO NPC
    # ========================================================

    call iniciar_encontro_npc

    # ========================================================
    # INTRODUÇÃO DO NÁUFRAGO
    # ========================================================

    naufrago "Ei! Vocês aí!"


    naufrago "Não esperava encontrar outro navio por aqui."


    # Por enquanto ainda não existem escolhas.
    #
    # Na próxima etapa entraremos aqui com:
    #
    # - opções de diálogo;
    # - impactos positivos/negativos;
    # - atualização da Disposição.


    # ========================================================
    # ENCERRA O ENCONTRO
    # ========================================================

    call encerrar_encontro_npc


    return
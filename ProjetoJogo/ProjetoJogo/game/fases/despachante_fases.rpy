# ============================================================
# DESPACHANTE DE CONTEÚDO DAS FASES
# ============================================================

# Este arquivo faz a ligação entre a lógica geral do jogo
# e o conteúdo específico de cada fase.


label exibir_ilha_atual:


    # ========================================================
    # FASE 1
    # ========================================================

    if fase_atual == 1:

        call fase_1_exibir_estado


    # ========================================================
    # FASES WIP
    # ========================================================

    elif fase_atual == 2:

        "O conteúdo da Fase 2 ainda não foi implementado."


    elif fase_atual == 3:

        "O conteúdo da Fase 3 ainda não foi implementado."


    elif fase_atual == 4:

        "O conteúdo da Fase 4 ainda não foi implementado."


    elif fase_atual == 5:

        "O conteúdo da Fase 5 ainda não foi implementado."


    elif fase_atual == 6:

        "O conteúdo da Fase 6 ainda não foi implementado."


    elif fase_atual == 7:

        "O conteúdo da Fase 7 ainda não foi implementado."


    else:

        "Erro: fase desconhecida."


    return

# ============================================================
# DESPACHANTE DO MAPA
# ============================================================

screen mapa_atual:

    modal True


    if fase_atual == 1:

        use mapa_fase_1


    elif fase_atual == 2:

        frame:

            xalign 0.5
            yalign 0.5

            text "Mapa da Fase 2 ainda não implementado."


    else:

        frame:

            xalign 0.5
            yalign 0.5

            text "Mapa desta fase ainda não disponível."
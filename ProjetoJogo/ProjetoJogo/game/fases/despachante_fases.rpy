# ============================================================
# DESPACHANTE DE CONTEÚDO DAS FASES
# ============================================================

# FAz a ligação entre a lógica geral do jogo
# e o conteúdo específico de cada fase.


# ============================================================
# PREPARAR FASE ATUAL
# ============================================================

label preparar_fase_atual:


    if fase_atual == 1:

        call fase_1_preparar


    elif fase_atual == 2:

        pass


    elif fase_atual == 3:

        pass


    elif fase_atual == 4:

        pass


    elif fase_atual == 5:

        pass


    elif fase_atual == 6:

        pass


    elif fase_atual == 7:

        pass


    return



# ============================================================
# PEDIR DICA DA FASE ATUAL
# ============================================================

label pedir_dica_atual:


    if fase_atual == 1:

        call fase_1_pedir_dica


    elif fase_atual == 2:

        navegador "Ainda não existem dicas para esta fase."


    elif fase_atual == 3:

        navegador "Ainda não existem dicas para esta fase."


    elif fase_atual == 4:

        navegador "Ainda não existem dicas para esta fase."


    elif fase_atual == 5:

        navegador "Ainda não existem dicas para esta fase."


    elif fase_atual == 6:

        navegador "Ainda não existem dicas para esta fase."


    elif fase_atual == 7:

        navegador "Ainda não existem dicas para esta fase."


    return



# ============================================================
# DICA DO NPC DA FASE ATUAL
# ============================================================

label fornecer_dica_npc_atual:


    if fase_atual == 1:

        call fase_1_fornecer_dica_npc


    elif fase_atual == 2:

        naufrago "Ainda não tenho informações sobre esta fase."


    elif fase_atual == 3:

        naufrago "Ainda não tenho informações sobre esta fase."


    elif fase_atual == 4:

        naufrago "Ainda não tenho informações sobre esta fase."


    elif fase_atual == 5:

        naufrago "Ainda não tenho informações sobre esta fase."


    elif fase_atual == 6:

        naufrago "Ainda não tenho informações sobre esta fase."


    elif fase_atual == 7:

        naufrago "Ainda não tenho informações sobre esta fase."


    return



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
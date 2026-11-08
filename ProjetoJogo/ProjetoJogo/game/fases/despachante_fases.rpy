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
        call fase_2_preparar


    elif fase_atual == 3:
        call fase_3_preparar


    elif fase_atual == 4:
        call fase_4_preparar


    elif fase_atual == 5:
        call fase_5_preparar


    elif fase_atual == 6:
        call fase_6_preparar
        

    elif fase_atual == 7:
        call fase_7_preparar

    return



# ============================================================
# PEDIR DICA DA FASE ATUAL
# ============================================================

label pedir_dica_atual:


    if fase_atual == 1:

        call fase_1_pedir_dica


    elif fase_atual == 2:

        call fase_2_pedir_dica


    elif fase_atual == 3:

        call fase_3_pedir_dica


    elif fase_atual == 4:

        call fase_4_pedir_dica


    elif fase_atual == 5:

        call fase_5_pedir_dica


    elif fase_atual == 6:

        call fase_6_pedir_dica


    elif fase_atual == 7:

        call fase_7_pedir_dica


    return



# ============================================================
# DICA DO NPC DA FASE ATUAL
# ============================================================

label fornecer_dica_npc_atual:


    if fase_atual == 1:

        call fase_1_fornecer_dica_npc


    elif fase_atual == 2:

        call fase_2_fornecer_dica_npc


    elif fase_atual == 3:

        call fase_3_fornecer_dica_npc


    elif fase_atual == 4:

        call fase_4_fornecer_dica_npc


    elif fase_atual == 5:

        call fase_5_fornecer_dica_npc


    elif fase_atual == 6:

        call fase_6_fornecer_dica_npc


    elif fase_atual == 7:

        call fase_7_fornecer_dica_npc


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

        call fase_2_exibir_estado

    elif fase_atual == 3:

        call fase_3_exibir_estado


    elif fase_atual == 4:

        call fase_4_exibir_estado


    elif fase_atual == 5:

        call fase_5_exibir_estado


    elif fase_atual == 6:

        call fase_6_exibir_estado   


    elif fase_atual == 7:

        call fase_7_exibir_estado


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


# ============================================================
# INTRODUÇÃO DA FASE ATUAL
# ============================================================

label introducao_fase_atual:


    if fase_atual == 1:

        call fase_1_introducao


    elif fase_atual == 2:

        call fase_2_introducao


    elif fase_atual == 3:

        call fase_3_introducao


    elif fase_atual == 4:

        call fase_4_introducao


    elif fase_atual == 5:

        call fase_5_introducao


    elif fase_atual == 6:

        call fase_6_introducao


    elif fase_atual == 7:

        call fase_7_introducao


    return
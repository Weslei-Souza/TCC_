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


# ============================================================
# EXIBIR ESTADO ATUAL
# ============================================================

label exibir_ilha_atual:


    # O visual é agora genérico.
    #
    # A configuração formal continua pertencendo à fase,
    # mas estados comuns, finais e armadilhas utilizam
    # fundos compartilhados.

    call exibir_estado_visual


    return


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
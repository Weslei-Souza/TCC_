# ============================================================
# MOTOR GERAL DE EVENTOS DOS ESTADOS
# ============================================================

# Este arquivo é executado sempre que o jogador
# CHEGA a um novo estado.
#
# Ele decide genericamente se o estado representa:
#
# - vitória;
# - armadilha;
# - ilha intermediária com possível NPC;
# - estado normal.


# ============================================================
# PROCESSAR CHEGADA AO ESTADO ATUAL
# ============================================================

label processar_eventos_estado_atual:


    # ========================================================
    # ESTADO FINAL
    # ========================================================

    if automato.eh_final(
        configuracao_automato,
        estado_atual
    ):

        return "vitoria"


    # ========================================================
    # ESTADO DE ARMADILHA
    # ========================================================

    if automato.eh_armadilha(
        configuracao_automato,
        estado_atual
    ):

        # Cada entrada em uma armadilha representa
        # uma nova ocorrência da métrica.

        $ armadilhas_atingidas += 1


        # A Necessidade de Assistência deve refletir
        # imediatamente a nova ocorrência.

        call atualizar_necessidade_assistencia


        # Inicia o fluxo de Game Over.

        call game_over_armadilha

        $ resultado_game_over = _return


        return resultado_game_over


    # ========================================================
    # ESTADO INTERMEDIÁRIO
    # ========================================================

    if automato.eh_intermediario(
        configuracao_automato,
        estado_atual
    ):

        # O próprio controlador de NPC decide:
        #
        # - se a fase possui NPC;
        # - se é fixo ou aleatório;
        # - se ainda pode aparecer;
        # - se o sorteio foi bem-sucedido.

        call verificar_encontro_npc_atual


    return "continuar"



# ============================================================
# GAME OVER - ARMADILHA
# ============================================================

label game_over_armadilha:


    $ nome_armadilha = automato.nome_estado(
        configuracao_automato,
        estado_atual
    )


    "Você chegou a [nome_armadilha]."


    navegador "Capitão, não podemos continuar daqui!"


    menu:

        "Reiniciar a fase":

            # Reiniciar também incrementa numero_resets,
            # conforme a definição das métricas.

            call reiniciar_fase

            return "reiniciado"


        "Voltar ao Menu":

            # Sair pelo menu não conta como reinício.

            return "menu"
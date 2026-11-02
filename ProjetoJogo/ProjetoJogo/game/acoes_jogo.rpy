# ============================================================
# AÇÕES GERAIS DO JOGO
# ============================================================


# ============================================================
# REINICIAR FASE
# ============================================================

label reiniciar_fase:

    # --------------------------------------------------------
    # ENCERRA A TENTATIVA ATUAL
    # --------------------------------------------------------

    # Um reinício significa que a tentativa atual terminou
    # e uma nova tentativa começou.

    $ numero_resets += 1

    $ numero_tentativas += 1


    # --------------------------------------------------------
    # VOLTA AO ESTADO INICIAL
    # --------------------------------------------------------

    $ estado_atual = automato.estado_inicial(
        configuracao_automato
    )


    # --------------------------------------------------------
    # REINICIA O PERCURSO ATUAL
    # --------------------------------------------------------

    # As métricas acumuladas da fase NÃO são apagadas.
    #
    # Apenas o percurso da nova tentativa começa novamente
    # no estado inicial.

    $ historico_estados = [estado_atual]


    navegador "Vamos recomeçar o percurso, capitão."


    return
# 
# AÇÕES GERAIS DO JOGO


# ============================================================
# ATUALIZAR NECESSIDADE DE ASSISTÊNCIA
# ============================================================

label atualizar_necessidade_assistencia:

    # Obtém os limites definidos especificamente
    # para a fase atual.

    $ limites_assistencia = configuracao_automato.get(
        "limites_assistencia",
        {}
    )


    # Calcula o índice atual entre 0 e 100.

    $ necessidade_assistencia = jogador.calcular_necessidade_assistencia(
        numero_resets,
        dicas_pedidas,
        estados_repetidos,
        armadilhas_atingidas,
        limites_assistencia
    )

    "DEBUG - Necessidade de Assistência: [necessidade_assistencia]"

    return

#############
# REINICIAR FASE


label reiniciar_fase:

    # Registra o reinício.
    $ numero_resets += 1

    #atualiza o indice de necessidade 
    call atualizar_necessidade_assistencia 

    #retorna ao estado inicial 
    $ estado_atual = automato.estado_inicial(
        configuracao_automato
    )


    # O percurso atual começa novamente no estado inicial.
    $ historico_estados = [estado_atual]


    navegador "Vamos recomeçar o percurso, capitão."


    return
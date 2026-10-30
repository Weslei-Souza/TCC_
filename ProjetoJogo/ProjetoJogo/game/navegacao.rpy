# ============================================================
# MODO DE NAVEGAÇÃO PASSO A PASSO
# ============================================================

label modo_navegacao:

    call exibir_ilha_atual


    # ========================================================
    # VERIFICA SE O ESTADO ATUAL JÁ É FINAL
    # ========================================================

    if automato.eh_final(
        configuracao_automato,
        estado_atual
    ):

        jump vitoria


    # ========================================================
    # CONSULTA AS TRANSIÇÕES DISPONÍVEIS
    # ========================================================

    $ destino_a_estado = automato.transicao(
        configuracao_automato,
        estado_atual,
        "A"
    )

    $ destino_b_estado = automato.transicao(
        configuracao_automato,
        estado_atual,
        "B"
    )


    if destino_a_estado:

        $ destino_a = automato.nome_estado(
            configuracao_automato,
            destino_a_estado
        )

    else:

        $ destino_a = "Sem rota"


    if destino_b_estado:

        $ destino_b = automato.nome_estado(
            configuracao_automato,
            destino_b_estado
        )

    else:

        $ destino_b = "Sem rota"


    # ========================================================
    # MOSTRA AS OPÇÕES AO JOGADOR
    # ========================================================

    call screen escolha_transicao(
        automato.nome_estado(
            configuracao_automato,
            estado_atual
        ),
        destino_a,
        destino_b
    )


    $ simbolo = _return


    # ========================================================
    # CONTROLES GERAIS
    # ========================================================

    if simbolo == "__AJUDA__":

        call pedir_dica_atual
        # ========================================================
        # DEBUG TEMPORÁRIO
        # ========================================================

        "DEBUG - Histórico: [historico_estados]"
        "DEBUG - Repetições: [estados_repetidos]"
        "DEBUG - Retornos: [quantidade_retornos]"
        "DEBUG - Pedidos de ajuda: [pedidos_ajuda]"
        "DEBUG - Resets: [numero_resets]"
        "DEBUG - Dicas restantes: [len(dicas_disponiveis)]"


        jump modo_navegacao


    elif simbolo == "__REINICIAR__":

        call reiniciar_fase

        jump modo_navegacao


    # ========================================================
    # EXECUTA A TRANSIÇÃO
    # ========================================================

    $ proximo_estado = automato.transicao(
        configuracao_automato,
        estado_atual,
        simbolo
    )


    if proximo_estado is None:

        navegador "Não existe uma rota [simbolo] saindo desta ilha."

        jump modo_navegacao


    # ========================================================
    # REGISTRA A NAVEGAÇÃO DO JOGADOR
    # ========================================================

    $ novo_historico, novas_repeticoes, novos_retornos = jogador.registrar_percurso(
        historico_estados,
        [proximo_estado]
    )


    $ historico_estados = novo_historico
    $ estados_repetidos += novas_repeticoes
    $ quantidade_retornos += novos_retornos


    # ========================================================
    # ATUALIZA O ESTADO DA PARTIDA
    # ========================================================

    $ estado_atual = proximo_estado


    

    jump modo_navegacao



# ============================================================
# MODO DE PLANEJAMENTO DE ROTA
# ============================================================

label modo_rota:

    call exibir_ilha_atual


    # ========================================================
    # VERIFICA SE O ESTADO ATUAL JÁ É FINAL
    # ========================================================

    if automato.eh_final(
        configuracao_automato,
        estado_atual
    ):

        jump vitoria


    navegador "Capitão, podemos planejar várias rotas antes de partir."


    # ========================================================
    # RECEBE A ENTRADA DO JOGADOR
    # ========================================================

    call screen entrada_rota(
        automato.nome_estado(
            configuracao_automato,
            estado_atual
        )
    )


    $ entrada_jogador = _return


    # ========================================================
    # CONTROLES GERAIS
    # ========================================================

    if entrada_jogador == "__AJUDA__":

        call pedir_dica_atual

        jump modo_rota


    elif entrada_jogador == "__REINICIAR__":

        call reiniciar_fase

        jump modo_rota


    # ========================================================
    # TRATA A SEQUÊNCIA INFORMADA
    # ========================================================

    $ sequencia = entrada_jogador.strip().upper()


    # ========================================================
    # PROCESSA A SEQUÊNCIA NO AUTÔMATO
    # ========================================================

    $ novo_estado, caminho, erro = automato.processar_sequencia(
        configuracao_automato,
        estado_atual,
        sequencia
    )


    # Cria uma versão textual para apresentar na tela.

    $ percurso = " -> ".join(caminho)


    # O primeiro elemento é o estado em que o jogador
    # já estava antes de iniciar a sequência.

    $ estados_visitados = caminho[1:]


    # ========================================================
    # REGISTRA A NAVEGAÇÃO DO JOGADOR
    # ========================================================

    $ novo_historico, novas_repeticoes, novos_retornos = jogador.registrar_percurso(
        historico_estados,
        estados_visitados
    )


    $ historico_estados = novo_historico
    $ estados_repetidos += novas_repeticoes
    $ quantidade_retornos += novos_retornos


    # ========================================================
    # ATUALIZA O ESTADO ATUAL
    # ========================================================

    $ estado_atual = novo_estado


    # ========================================================
    # MOSTRA O RESULTADO
    # ========================================================

    "Sequência informada: [sequencia]"

    "Percurso realizado: [percurso]"


    # ========================================================
    # DEBUG TEMPORÁRIO
    # ========================================================

    "DEBUG - Histórico: [historico_estados]"
    "DEBUG - Repetições: [estados_repetidos]"
    "DEBUG - Retornos: [quantidade_retornos]"
    "DEBUG - Pedidos de ajuda: [pedidos_ajuda]"
    "DEBUG - Resets: [numero_resets]"
    "DEBUG - Dicas restantes: [len(dicas_disponiveis)]"


    # ========================================================
    # TRATA POSSÍVEIS ERROS
    # ========================================================

    if erro:

        navegador "[erro]"


    # ========================================================
    # VERIFICA VITÓRIA
    # ========================================================

    if automato.eh_final(
        configuracao_automato,
        estado_atual
    ):

        jump vitoria


    navegador "Terminamos em [automato.nome_estado(configuracao_automato, estado_atual)]."

    navegador "Podemos planejar outra rota daqui."


    jump modo_rota



# ============================================================
# VITÓRIA
# ============================================================

label vitoria:

    call exibir_ilha_atual


    navegador "Capitão, encontramos nosso destino!"

    "Você concluiu a Fase [fase_atual]."


    # ========================================================
    # DESBLOQUEAR A PRÓXIMA FASE
    # ========================================================

    if fase_atual < 7:

        $ proxima_fase = fase_atual + 1


        if persistent.fase_max_desbloqueada < proxima_fase:

            $ persistent.fase_max_desbloqueada = proxima_fase

            $ renpy.save_persistent()


            "Uma nova fase foi desbloqueada!"


    return
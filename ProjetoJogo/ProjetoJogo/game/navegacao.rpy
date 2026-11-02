# ============================================================
# MODO DE NAVEGAÇÃO PASSO A PASSO
# ============================================================

label modo_navegacao:

    call exibir_ilha_atual


    # ========================================================
    # VERIFICA SE O ESTADO ATUAL É FINAL
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

        jump modo_navegacao


    elif simbolo == "__REINICIAR__":

        call reiniciar_fase

        jump modo_navegacao


    elif simbolo == "__MENU__":

        # A tentativa atual é encerrada por abandono.
        #
        # Não incrementamos numero_tentativas aqui porque
        # esta tentativa já foi contabilizada quando começou.
        #
        # Como nenhuma nova tentativa começa, apenas
        # encerramos a execução da partida.

        return


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

    $ novo_historico, novas_repeticoes = jogador.registrar_percurso(
        historico_estados,
        [proximo_estado]
    )


    $ historico_estados = novo_historico

    $ estados_repetidos += novas_repeticoes


    # ========================================================
    # ATUALIZA O ESTADO
    # ========================================================

    $ estado_atual = proximo_estado


    jump modo_navegacao



# ============================================================
# MODO DE PLANEJAMENTO DE ROTA
# ============================================================

label modo_rota:

    call exibir_ilha_atual


    # ========================================================
    # VERIFICA SE O ESTADO ATUAL É FINAL
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


    elif entrada_jogador == "__MENU__":

        # Encerra a tentativa atual por abandono.

        return


    # ========================================================
    # TRATA A SEQUÊNCIA
    # ========================================================

    $ sequencia = entrada_jogador.strip().upper()


    # ========================================================
    # PROCESSA A SEQUÊNCIA
    # ========================================================

    $ novo_estado, caminho, erro = automato.processar_sequencia(
        configuracao_automato,
        estado_atual,
        sequencia
    )


    # Cria uma representação textual do percurso.

    $ percurso = " -> ".join(caminho)


    # O primeiro elemento já era o estado atual,
    # então não deve ser registrado novamente.

    $ estados_visitados = caminho[1:]


    # ========================================================
    # REGISTRA A NAVEGAÇÃO
    # ========================================================

    $ novo_historico, novas_repeticoes = jogador.registrar_percurso(
        historico_estados,
        estados_visitados
    )


    $ historico_estados = novo_historico

    $ estados_repetidos += novas_repeticoes


    # ========================================================
    # ATUALIZA O ESTADO
    # ========================================================

    $ estado_atual = novo_estado


    # ========================================================
    # MOSTRA O RESULTADO
    # ========================================================

    "Sequência informada: [sequencia]"

    "Percurso realizado: [percurso]"


    # ========================================================
    # TRATA ERROS
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


    # A tentativa atual foi encerrada com sucesso.
    #
    # Não incrementamos numero_tentativas porque ela já
    # foi contabilizada quando começou.


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
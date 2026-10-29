====
# MODO DE NAVEGAÇÃO PASSO A PASS====

label modo_navegacao:

    call exibir_ilha_atual

    if automato.eh_final(estado_atual):
        jump vitoria


    # Consulta ao módulo Python quais estados são alcançados
    # pelas transições A e B.

    $ destino_a_estado = automato.transicao(estado_atual, "A")
    $ destino_b_estado = automato.transicao(estado_atual, "B")


    if destino_a_estado:
        $ destino_a = automato.nome_estado(destino_a_estado)
    else:
        $ destino_a = "Sem rota"


    if destino_b_estado:
        $ destino_b = automato.nome_estado(destino_b_estado)
    else:
        $ destino_b = "Sem rota"


    # Mostra as opções disponíveis para o jogador.

    call screen escolha_transicao(
        automato.nome_estado(estado_atual),
        destino_a,
        destino_b
    )


    $ simbolo = _return


    # Envia ao módulo do autômato:
    #
    # estado atual + símbolo escolhido
    #
    # e recebe o próximo estado.

    $ proximo_estado = automato.transicao(
        estado_atual,
        simbolo
    )


    if proximo_estado is None:

        navegador "Não existe uma rota [simbolo] saindo desta ilha."

        jump modo_navegacao


    # REGISTRO DA NAVEGAÇÃO DO JOGADOR

    $ novo_historico, novas_repeticoes, novos_retornos = jogador.registrar_percurso(
        historico_estados,
        [proximo_estado]
    )


    $ historico_estados = novo_historico

    $ estados_repetidos += novas_repeticoes
    $ quantidade_retornos += novos_retornos


    # Atualiza o estado da partida.

    $ estado_atual = proximo_estado


    jump modo_navegacao

====
# MODO DE PLANEJAMENTO DE ROT====

label modo_rota:

    call exibir_ilha_atual


    if automato.eh_final(estado_atual):
        jump vitoria


    navegador "Capitão, podemos planejar várias rotas antes de partir."


    call screen entrada_rota(
        automato.nome_estado(estado_atual)
    )


    $ sequencia = _return.strip().upper()


    # O módulo Python processa toda a sequência.

    $ novo_estado, caminho, erro = automato.processar_sequencia(
        estado_atual,
        sequencia
    )


    # Cria uma versão textual apenas para mostrar na tela.

    $ percurso = " -> ".join(caminho)


    # O primeiro elemento é o estado em que o jogador já estava.
    # Portanto, registramos apenas os estados seguintes.

    $ estados_visitados = caminho[1:]


    # REGISTRO DA NAVEGAÇÃO DO JOGADOR

    $ novo_historico, novas_repeticoes, novos_retornos = jogador.registrar_percurso(
        historico_estados,
        estados_visitados
    )


    $ historico_estados = novo_historico

    $ estados_repetidos += novas_repeticoes
    $ quantidade_retornos += novos_retornos


    # Atualiza onde o jogador terminou.

    $ estado_atual = novo_estado


    "Sequência informada: [sequencia]"

    "Percurso realizado: [percurso]"


    if erro:

        navegador "[erro]"


    if automato.eh_final(estado_atual):

        jump vitoria


    navegador "Terminamos em [automato.nome_estado(estado_atual)]."

    navegador "Podemos planejar outra rota daqui."


    jump modo_rota

====
# VITÓRI====

label vitoria:

    call exibir_ilha_atual


    navegador "Capitão, encontramos nosso destino!"

    "Você concluiu a Fase [fase_atual]."


    # DESBLOQUEAR A PRÓXIMA FASE

    if fase_atual < 7:

        $ proxima_fase = fase_atual + 1


        if persistent.fase_max_desbloqueada < proxima_fase:

            $ persistent.fase_max_desbloqueada = proxima_fase

            $ renpy.save_persistent()


            "Uma nova fase foi desbloqueada!"


    return
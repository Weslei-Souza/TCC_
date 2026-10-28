label modo_navegacao:

    call exibir_ilha_atual

    if automato.eh_final(estado_atual):
        jump vitoria


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


    call screen escolha_transicao(
        automato.nome_estado(estado_atual),
        destino_a,
        destino_b
    )


    $ simbolo = _return

    $ proximo_estado = automato.transicao(
        estado_atual,
        simbolo
    )


    if proximo_estado is None:

        navegador "Não existe uma rota [simbolo] saindo desta ilha."

        jump modo_navegacao


    $ estado_atual = proximo_estado

    jump modo_navegacao



label modo_rota:

    call exibir_ilha_atual

    if automato.eh_final(estado_atual):
        jump vitoria


    navegador "Capitão, podemos planejar várias rotas antes de partir."

    call screen entrada_rota(
        automato.nome_estado(estado_atual)
    )


    $ sequencia = _return.strip().upper()


    $ novo_estado, percurso, erro = automato.processar_sequencia(
        estado_atual,
        sequencia
    )


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


    label vitoria:

    call exibir_ilha_atual

    navegador "Capitão, encontramos nosso destino!"

    "Você concluiu o percurso."

    return
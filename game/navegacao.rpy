# ============================================================
# MODO NAVEGAÇÃO PASSO A PASSO
# ============================================================

label modo_navegacao:


    # Mostra o estado inicial.

    call exibir_ilha_atual from _call_exibir_ilha_atual


    jump navegacao_escolher_transicao



# ============================================================
# ESCOLHER PRÓXIMA TRANSIÇÃO
# ============================================================

label navegacao_escolher_transicao:


    # ========================================================
    # DESTINOS
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
    # ESCOLHA
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
    # DICA
    # ========================================================

    if simbolo == "__AJUDA__":

        call pedir_dica_atual from _call_pedir_dica_atual

        jump navegacao_escolher_transicao


    # ========================================================
    # REINICIAR
    # ========================================================

    elif simbolo == "__REINICIAR__":

        call reiniciar_fase from _call_reiniciar_fase_1

        call exibir_ilha_atual from _call_exibir_ilha_atual_1

        jump navegacao_escolher_transicao


    # ========================================================
    # MENU
    # ========================================================

    elif simbolo == "__MENU__":

        return


    # ========================================================
    # EXECUTA TRANSIÇÃO
    # ========================================================

    $ proximo_estado = automato.transicao(
        configuracao_automato,
        estado_atual,
        simbolo
    )


    if proximo_estado is None:

        navegador "Não existe uma rota [simbolo] saindo desta ilha."

        jump navegacao_escolher_transicao


    # ========================================================
    # REGISTRA PERCURSO
    # ========================================================

    $ novo_historico, novas_repeticoes = jogador.registrar_percurso(
        historico_estados,
        [proximo_estado]
    )


    $ historico_estados = novo_historico

    $ estados_repetidos += novas_repeticoes


    call atualizar_necessidade_assistencia from _call_atualizar_necessidade_assistencia_10


    # ========================================================
    # ATUALIZA ESTADO
    # ========================================================

    $ estado_atual = proximo_estado


    # Mostra visualmente a nova ilha.

    call exibir_ilha_atual from _call_exibir_ilha_atual_2


    # ========================================================
    # PROCESSA EVENTOS DA CHEGADA
    # ========================================================

    call processar_eventos_estado_atual from _call_processar_eventos_estado_atual

    $ resultado_evento = _return


    # ========================================================
    # VITÓRIA
    # ========================================================

    if resultado_evento == "vitoria":

        jump vitoria


    # ========================================================
    # GAME OVER + REINÍCIO
    # ========================================================

    elif resultado_evento == "reiniciado":

        call exibir_ilha_atual from _call_exibir_ilha_atual_3

        jump navegacao_escolher_transicao


    # ========================================================
    # GAME OVER + MENU
    # ========================================================

    elif resultado_evento == "menu":

        return


    jump navegacao_escolher_transicao

#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————


# ============================================================
# MODO PLANEJAMENTO DE ROTA
# ============================================================

label modo_rota:


    call exibir_ilha_atual from _call_exibir_ilha_atual_4


    jump planejar_nova_rota



# ============================================================
# PLANEJAR NOVA ROTA
# ============================================================

label planejar_nova_rota:


    navegador "Capitão, podemos planejar várias rotas antes de partir."


    call screen entrada_rota(
        automato.nome_estado(
            configuracao_automato,
            estado_atual
        )
    )


    $ entrada_jogador = _return


    # ========================================================
    # DICA
    # ========================================================

    if entrada_jogador == "__AJUDA__":

        call pedir_dica_atual from _call_pedir_dica_atual_1

        jump planejar_nova_rota


    # ========================================================
    # REINICIAR
    # ========================================================

    elif entrada_jogador == "__REINICIAR__":

        call reiniciar_fase from _call_reiniciar_fase_2

        call exibir_ilha_atual from _call_exibir_ilha_atual_5

        jump planejar_nova_rota


    # ========================================================
    # MENU
    # ========================================================

    elif entrada_jogador == "__MENU__":

        return


    # ========================================================
    # PREPARA SEQUÊNCIA
    # ========================================================

    $ sequencia = entrada_jogador.strip().replace(
        " ",
        ""
    ).upper()


    if not sequencia:

        navegador "Nenhuma rota foi informada."

        jump planejar_nova_rota


    # Caminho exibido ao jogador.

    $ caminho_exibicao = [
        automato.nome_estado(
            configuracao_automato,
            estado_atual
        )
    ]


    $ indice_rota = 0

    $ rota_interrompida = False

    $ resultado_evento = "continuar"


    # ========================================================
    # EXECUTA A SEQUÊNCIA PASSO A PASSO
    # ========================================================

    while (
        indice_rota < len(sequencia)
        and not rota_interrompida
    ):


        $ simbolo_rota = sequencia[
            indice_rota
        ]


        # ====================================================
        # SÍMBOLO INVÁLIDO
        # ====================================================

        if simbolo_rota not in automato.obter_alfabeto(
            configuracao_automato
        ):

            navegador "Símbolo inválido: [simbolo_rota]."

            $ rota_interrompida = True


        else:


            # ================================================
            # TRANSIÇÃO
            # ================================================

            $ proximo_estado = automato.transicao(
                configuracao_automato,
                estado_atual,
                simbolo_rota
            )


            if proximo_estado is None:

                navegador "Não existe uma rota [simbolo_rota] a partir de [automato.nome_estado(configuracao_automato, estado_atual)]."

                $ rota_interrompida = True


            else:


                # ============================================
                # MÉTRICAS
                # ============================================

                $ novo_historico, novas_repeticoes = jogador.registrar_percurso(
                    historico_estados,
                    [proximo_estado]
                )


                $ historico_estados = novo_historico

                $ estados_repetidos += novas_repeticoes


                call atualizar_necessidade_assistencia from _call_atualizar_necessidade_assistencia_11


                # ============================================
                # ATUALIZA ESTADO
                # ============================================

                $ estado_atual = proximo_estado


                $ caminho_exibicao.append(
                    automato.nome_estado(
                        configuracao_automato,
                        estado_atual
                    )
                )


                # Mostra cada estado efetivamente visitado.

                call exibir_ilha_atual from _call_exibir_ilha_atual_6


                # ============================================
                # EVENTOS
                # ============================================

                call processar_eventos_estado_atual from _call_processar_eventos_estado_atual_1

                $ resultado_evento = _return


                # ============================================
                # VITÓRIA
                # ============================================

                if resultado_evento == "vitoria":

                    $ percurso = " -> ".join(
                        caminho_exibicao
                    )

                    "Percurso realizado: [percurso]"

                    jump vitoria


                # ============================================
                # ARMADILHA + REINÍCIO
                # ============================================

                elif resultado_evento == "reiniciado":

                    $ rota_interrompida = True


                # ============================================
                # ARMADILHA + MENU
                # ============================================

                elif resultado_evento == "menu":

                    return


                # ============================================
                # CONTINUA A SEQUÊNCIA
                # ============================================

                else:

                    $ indice_rota += 1


    # ========================================================
    # REINICIADO DURANTE A ROTA
    # ========================================================

    if resultado_evento == "reiniciado":

        navegador "A rota foi interrompida."

        call exibir_ilha_atual from _call_exibir_ilha_atual_7

        jump planejar_nova_rota


    # ========================================================
    # RESULTADO DA ROTA
    # ========================================================

    $ percurso = " -> ".join(
        caminho_exibicao
    )


    "Sequência informada: [sequencia]"

    "Percurso realizado: [percurso]"


    navegador "Terminamos em [automato.nome_estado(configuracao_automato, estado_atual)]."


    jump planejar_nova_rota

#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
#—————————————————————————————————————————————————————————————————————
# ============================================================
# VITÓRIA
# ============================================================

label vitoria:


    # ========================================================
    # VISUAL
    # ========================================================

    scene bg_final

    show ui_victory at marca_resultado

    with transicao_fade


    navegador "Capitão, encontramos nosso destino!"


    # ========================================================
    # FASE 7 - ENCERRAMENTO DO JOGO
    # ========================================================

    if fase_atual == 7:


        "Você chegou à Ilha do Tesouro."


        navegador "Conseguimos, Capitão!"


        navegador "Depois de atravessar todos os arquipélagos, finalmente encontramos o tesouro."


        "Você completou todas as fases do jogo!"


        $ renpy.save_persistent()


        # Encerrar o contexto atual retorna
        # ao menu principal.

        return


    # ========================================================
    # FASES 1 A 6
    # ========================================================

    "Você concluiu a Fase [fase_atual]."


    $ proxima_fase = fase_atual + 1


    if persistent.fase_max_desbloqueada < proxima_fase:


        $ persistent.fase_max_desbloqueada = proxima_fase


        $ renpy.save_persistent()


        "Uma nova fase foi desbloqueada!"


    jump selecionar_fase_jogo
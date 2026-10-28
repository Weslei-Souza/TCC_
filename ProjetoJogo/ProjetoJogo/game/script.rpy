init python:

    from logica import automato
    from logica import fases

    if persistent.fase_max_desbloqueada is None:
        persistent.fase_max_desbloqueada = 1

#personagens
define m = Character('Me', color="#c8c8ff")
define navegador = Character('Navegador', color="#c8ffc8")

define m = Character('Me', color="#c8c8ff")
define navegador = Character('Navegador', color="#c8ffc8")


# ESTADO DA PARTIDA
default estado_atual = "q0"
default fase_atual = 1
default modo_jogo = None


# MÉTRICAS DO JOGADOR
default numero_tentativas = 0
default quantidade_retornos = 0
default estados_repetidos = 0
default entradas_armadilha = 0
default pedidos_ajuda = 0

default historico_estados = []
default historico_interacoes = []


# ESTADO D NPC
default estado_afetivo_npc = 0.0
default historico_npc = []

#começo do jogo
label start:

    $ estado_atual = automato.ESTADO_INICIAL

    call screen menu_modo_jogo

    $ modo_jogo = _return

    if modo_jogo == "navegacao":
        jump modo_navegacao

    elif modo_jogo == "rota":
        jump modo_rota
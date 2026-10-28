init python:
    from logica import automato

define m = Character('Me', color="#c8c8ff")
define navegador = Character('Navegador', color="#c8ffc8")

default estado_atual = "q0"
default modo_jogo = None


label start:

    $ estado_atual = automato.ESTADO_INICIAL

    call screen menu_modo_jogo

    $ modo_jogo = _return

    if modo_jogo == "navegacao":
        jump modo_navegacao

    elif modo_jogo == "rota":
        jump modo_rota
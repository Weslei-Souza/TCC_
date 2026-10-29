init python:

    from logica import automato
    from logica import fases
    from logica import jogador

    # Se nunca houve progresso salvo,
    # somente a primeira fase fica liberada.
    if persistent.fase_max_desbloqueada is None:
        persistent.fase_max_desbloqueada = 1
#personagens
define m = Character('Me', color="#c8c8ff")
define navegador = Character('Navegador', color="#c8ffc8")

# ESTADO DA PARTIDA
default estado_atual = None
default fase_atual = 1
default modo_jogo = None
default configuracao_automato = None

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

label start:


    $ estados_repetidos = 0
    $ quantidade_retornos = 0
    $ numero_tentativas = 0
    $ entradas_armadilha = 0
    $ pedidos_ajuda = 0

    # 1. ESCOLHA DO MODO DE JOGO
    call screen menu_modo_jogo

    $ modo_jogo = _return


    # 2. ESCOLHA DA FASE
    call screen selecionar_fase

    $ fase_atual = _return

    # Obtém a configuração correspondente à fase escolhida.
    $ configuracao_automato = fases.obter_automato(
        fase_atual
    )


    $ estado_atual = automato.estado_inicial(
        configuracao_automato
    )
    # Reinicia as métricas da fase atual.
    $ historico_estados = [estado_atual]

    # 4. INÍCIO DO MODO ESCOLHIDO

    if modo_jogo == "navegacao":

        jump modo_navegacao


    elif modo_jogo == "rota":

        jump modo_rota
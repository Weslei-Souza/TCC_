# ============================================================
# IMPORTAÇÕES PYTHON
# ============================================================

init python:

    from logica import automato
    from logica import fases
    from logica import jogador

    # Se nunca houve progresso salvo,
    # somente a primeira fase fica liberada.
    if persistent.fase_max_desbloqueada is None:
        persistent.fase_max_desbloqueada = 1


# ============================================================
# PERSONAGENS
# ============================================================

define m = Character('Me', color="#c8c8ff")
define navegador = Character('Navegador', color="#c8ffc8")


# ============================================================
# ESTADO DA PARTIDA
# ============================================================

default estado_atual = None
default fase_atual = 1
default modo_jogo = None
default configuracao_automato = None


# ============================================================
# MÉTRICAS DO JOGADOR
# ============================================================

# Número de ciclos de execução da fase.
default numero_tentativas = 0

# Quantidade de vezes que o jogador visitou
# novamente um estado já percorrido.
default estados_repetidos = 0

# Quantidade de solicitações de dica.
default dicas_pedidas = 0

# Quantidade de vezes que a fase foi reiniciada.
default numero_resets = 0

# Quantidade de entradas em estados de armadilha.
# Será utilizada apenas nas fases que possuírem armadilhas.
default armadilhas_atingidas = 0


# ============================================================
# HISTÓRICOS
# ============================================================

default historico_estados = []
default historico_interacoes = []


# ============================================================
# SISTEMA DE DICAS
# ============================================================

default dicas_disponiveis = []
default ultima_dica = None


# ============================================================
# NPC
# ============================================================

# Disposição Afetiva do NPC.
#
# Futuramente será um valor contínuo entre 0 e 100
# e será fuzzificado nos conjuntos:
#
# Hostil / Neutro / Amigável
#
# O valor inicial ainda será definido.
default disposicao_npc = None

default historico_npc = []


# ============================================================
# INÍCIO DO JOGO
# ============================================================

label start:

    # ========================================================
    # 1. ESCOLHA DO MODO DE JOGO
    # ========================================================

    call screen menu_modo_jogo

    $ modo_jogo = _return


    # ========================================================
    # 2. ESCOLHA DA FASE
    # ========================================================

    call screen selecionar_fase

    $ fase_atual = _return


    # ========================================================
    # 3. CARREGA O AUTÔMATO DA FASE
    # ========================================================

    $ configuracao_automato = fases.obter_automato(
        fase_atual
    )


    $ estado_atual = automato.estado_inicial(
        configuracao_automato
    )


    # ========================================================
    # 4. INICIALIZA AS MÉTRICAS DA FASE
    # ========================================================

    $ historico_estados = [estado_atual]

    # A primeira tentativa começa no momento em que
    # o jogador inicia a fase.
    $ numero_tentativas = 1

    $ estados_repetidos = 0
    $ dicas_pedidas = 0
    $ numero_resets = 0
    $ armadilhas_atingidas = 0


    # ========================================================
    # 5. PREPARA CONTEÚDO ESPECÍFICO DA FASE
    # ========================================================

    call preparar_fase_atual


    # ========================================================
    # 6. INICIA O MODO ESCOLHIDO
    # ========================================================

    if modo_jogo == "navegacao":

        jump modo_navegacao


    elif modo_jogo == "rota":

        jump modo_rota
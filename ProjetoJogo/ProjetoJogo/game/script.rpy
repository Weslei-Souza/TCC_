# ============================================================
# IMPORTAÇÕES PYTHON
# ============================================================

init python:

    from logica import automato
    from logica import fases
    from logica import jogador
    from logica import npc
    from logica import fuzzy

    # Se nunca houve progresso salvo,
    # somente a primeira fase fica liberada.
    if persistent.fase_max_desbloqueada is None:
        persistent.fase_max_desbloqueada = 1


# ============================================================
# PERSONAGENS
# ============================================================

define navegador = Character(
    'Navegador', 
    color="#c8ffc8"
)


define naufrago = Character(
    'Náufrago',
    color="#ffd6a5"
)

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

# Valor calculado entre 0 e 100.
# Será utilizado futuramente como entrada do sistema fuzzy.
default necessidade_assistencia = 0.0


# ============================================================
# HISTÓRICOS
# ============================================================

default historico_estados = []
default historico_interacoes = []


# ============================================================
# SISTEMA DE DICAS
# ============================================================

default dicas_disponiveis = []


# ============================================================
# NPC
# ============================================================

# Disposição atual do NPC encontrado.
#
# Escala:
# 0 a 100.
#
# No texto acadêmico lembrar de chamar de Disposição Afetiva.
default disposicao_npc = None

# Classificação narrativa temporária:
# hostil
# neutro
# amigavel
# Não representa ainda a classificação fuzzy.
default classificacao_npc = None

# ve se existe um NPC participando
# de um encontro neste momento.
default npc_presente = False

# Quantidade de encontros realizados
# na fase atual.
default contador_encontros_npc = 0

# Histórico dos encontros
default historico_npc = []

# Último resultado calculado pelo sistema fuzzy.
default resultado_fuzzy = None

# Valor crisp da última saída fuzzy.
default valor_assistencia_fuzzy = None

# Categoria de assistência selecionada:
# nenhuma
# generica
# intermediaria
# especifica
default categoria_assistencia = None


# ============================================================
# INÍCIO DO JOGO
# ============================================================

label start:

    # ========================================================
    #  ESCOLHA DO MODO DE JOGO
    # ========================================================

    call screen menu_modo_jogo

    $ modo_jogo = _return


    # ========================================================
    #  ESCOLHA DA FASE
    # ========================================================

    call screen selecionar_fase

    $ fase_atual = _return


    # ========================================================
    #  CARREGA O AUTÔMATO DA FASE
    # ========================================================

    $ configuracao_automato = fases.obter_automato(
        fase_atual
    )


    $ estado_atual = automato.estado_inicial(
        configuracao_automato
    )


    # ========================================================
    # INICIALIZA AS MÉTRICAS DA FASE
    # ========================================================

    $ historico_estados = [estado_atual]

    # A primeira tentativa começa no momento em que
    # o jogador inicia a fase.

    $ estados_repetidos = 0
    $ dicas_pedidas = 0
    $ numero_resets = 0
    $ armadilhas_atingidas = 0
    $ necessidade_assistencia = 0.0

    # ========================================================
    # INICIALIZA O SISTEMA DE NPC
    # ========================================================

    $ npc_presente = False

    $ disposicao_npc = None

    $ classificacao_npc = None

    $ contador_encontros_npc = 0

    $ historico_npc = []

    $ historico_interacoes = []



    $ resultado_fuzzy = None

    $ valor_assistencia_fuzzy = None
    
    $ categoria_assistencia = None

    # ========================================================
    # PREPARA CONTEÚDO ESPECÍFICO DA FASE
    # ========================================================

    call preparar_fase_atual


    # ========================================================
    # INICIA O MODO ESCOLHIDO
    # ========================================================

    if modo_jogo == "navegacao":

        jump modo_navegacao


    elif modo_jogo == "rota":

        jump modo_rota
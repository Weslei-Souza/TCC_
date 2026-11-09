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
# DESATIVA O GAME MENU PADRÃO DO REN'PY
# ============================================================

# O jogo possui navegação e controles próprios.
#
# Portanto, ESC/clique direito não devem abrir
# o menu padrão opaco do Ren'Py.

if "game_menu" in config.keymap:

    config.keymap[
        "game_menu"
    ] = []


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

# Dicas já fornecidas por NPCs na execução atual da fase.
# Cada categoria possui seu próprio histórico para impedir
# repetição enquanto ainda houver dicas não utilizadas.

default dicas_npc_usadas = {
    "generica": [],
    "intermediaria": [],
    "especifica": [],
}


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

    jump escolher_modo_jogo



# ============================================================
# ESCOLHER MODO
# ============================================================

label escolher_modo_jogo:


    call screen menu_modo_jogo

    $ escolha_modo = _return


    # ========================================================
    # VOLTAR AO MENU PRINCIPAL
    # ========================================================

    if escolha_modo == "__VOLTAR__":

        return


    $ modo_jogo = escolha_modo


    jump selecionar_fase_jogo



# ============================================================
# SELECIONAR FASE
# ============================================================

label selecionar_fase_jogo:


    call screen selecionar_fase

    $ escolha_fase = _return


    # ========================================================
    # VOLTAR À ESCOLHA DO MODO
    # ========================================================

    if escolha_fase == "__VOLTAR__":

        jump escolher_modo_jogo


    $ fase_atual = escolha_fase


    jump preparar_execucao_fase


# ============================================================
# PREPARAR EXECUÇÃO DA FASE
# ============================================================

label preparar_execucao_fase:


    # ========================================================
    # CARREGA E VALIDA A CONFIGURAÇÃO
    # ========================================================

    $ configuracao_automato = fases.obter_automato(
        fase_atual
    )


    # ========================================================
    # ESTADO INICIAL
    # ========================================================

    $ estado_atual = automato.estado_inicial(
        configuracao_automato
    )


    # ========================================================
    # MÉTRICAS
    # ========================================================

    $ historico_estados = [
        estado_atual
    ]

    $ estados_repetidos = 0

    $ dicas_pedidas = 0

    $ numero_resets = 0

    $ armadilhas_atingidas = 0

    $ necessidade_assistencia = 0.0


    # ========================================================
    # NPC
    # ========================================================

    $ npc_presente = False

    $ disposicao_npc = None

    $ classificacao_npc = None

    $ contador_encontros_npc = 0

    $ historico_npc = []

    $ historico_interacoes = []

    $ dicas_npc_usadas = {
    "generica": [],
    "intermediaria": [],
    "especifica": [],
}


    # ========================================================
    # FUZZY
    # ========================================================

    $ resultado_fuzzy = None

    $ valor_assistencia_fuzzy = None

    $ categoria_assistencia = None


    # ========================================================
    # CONTEÚDO DA FASE
    # ========================================================

    call preparar_fase_atual

    call introducao_fase_atual


    # ========================================================
    # INICIA O MODO
    # ========================================================

    if modo_jogo == "navegacao":

        jump modo_navegacao


    elif modo_jogo == "rota":

        jump modo_rota
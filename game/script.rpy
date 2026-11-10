# ============================================================
# CONFIGURAÇÕES GERAIS
# ============================================================

# Impede ESC e clique direito de abrirem
# o game menu padrão do Ren'Py.

define _game_menu_screen = None


# ============================================================
# TRANSIÇÕES
# ============================================================

define transicao_tela = Dissolve(0.25)

define transicao_fade = Fade(
    0.20,
    0.10,
    0.20
)


define config.intra_transition = transicao_tela

define config.enter_yesno_transition = transicao_tela

define config.exit_yesno_transition = transicao_tela

define config.end_game_transition = transicao_fade


# ============================================================
# SAÍDA DO JOGO
# ============================================================

define config.quit_action = Confirm(
    "Deseja realmente fechar o jogo?",
    Quit(confirm=False)
)


# ============================================================
# IMPORTAÇÕES PYTHON
# ============================================================

init python:

    from logica import automato
    from logica import fases
    from logica import jogador
    from logica import npc
    from logica import fuzzy


    # ========================================================
    # PROGRESSÃO
    # ========================================================

    if persistent.fase_max_desbloqueada is None:

        persistent.fase_max_desbloqueada = 1


    # ========================================================
    # F11 - TELA CHEIA
    # ========================================================

    if (
        "toggle_fullscreen" in config.keymap
        and "K_F11"
        not in config.keymap["toggle_fullscreen"]
    ):

        config.keymap[
            "toggle_fullscreen"
        ].append(
            "K_F11"
        )



# ============================================================
# PERSONAGENS
# ============================================================

define navegador = Character(
    "Navegador",
    color="#83D5FF",
    image="navegador"
)


define naufrago = Character(
    "Náufrago",
    color="#F1C75B",
    image="naufrago"
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

default estados_repetidos = 0

default dicas_pedidas = 0

default numero_resets = 0

default armadilhas_atingidas = 0

default necessidade_assistencia = 0.0



# ============================================================
# HISTÓRICOS
# ============================================================

default historico_estados = []

default historico_interacoes = []



# ============================================================
# DICAS
# ============================================================

default dicas_disponiveis = []


default dicas_npc_usadas = {

    "generica": [],

    "intermediaria": [],

    "especifica": [],
}



# ============================================================
# NPC
# ============================================================

default disposicao_npc = None

default classificacao_npc = None

default npc_presente = False

default contador_encontros_npc = 0

default historico_npc = []


default resultado_fuzzy = None

default valor_assistencia_fuzzy = None

default categoria_assistencia = None



# ============================================================
# INÍCIO
# ============================================================

label start:


    jump escolher_modo_jogo



# ============================================================
# ESCOLHER MODO
# ============================================================

label escolher_modo_jogo:


    call screen menu_modo_jogo(
        _with_none=False
    ) with transicao_tela


    with transicao_tela


    $ escolha_modo = _return


    # Voltar ao menu principal.

    if escolha_modo == "__VOLTAR__":

        return


    $ modo_jogo = escolha_modo


    jump selecionar_fase_jogo



# ============================================================
# SELECIONAR FASE
# ============================================================

label selecionar_fase_jogo:


    call screen selecionar_fase(
        _with_none=False
    ) with transicao_tela


    with transicao_tela


    $ escolha_fase = _return


    if escolha_fase == "__VOLTAR__":

        jump escolher_modo_jogo


    $ fase_atual = escolha_fase


    jump preparar_execucao_fase



# ============================================================
# PREPARAR FASE
# ============================================================

label preparar_execucao_fase:


    # ========================================================
    # CONFIGURAÇÃO
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
    # PREPARAÇÃO DA FASE
    # ========================================================

    call preparar_fase_atual from _call_preparar_fase_atual


    # Fundo da introdução.

    scene bg_mar

    with transicao_fade


    call introducao_fase_atual from _call_introducao_fase_atual


    # ========================================================
    # MODO
    # ========================================================

    if modo_jogo == "navegacao":

        jump modo_navegacao


    elif modo_jogo == "rota":

        jump modo_rota
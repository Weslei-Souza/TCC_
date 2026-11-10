# ============================================================
# CAMADA VISUAL DO JOGO
# ============================================================
#
# Centraliza:
# - imagens;
# - personagens visuais;
# - fundos;
# - mapas;
# - cores;
# - estilos;
# - telas principais.
#
# A lógica do jogo permanece fora deste arquivo.
# ============================================================


# As definições deste arquivo devem prevalecer
# sobre as telas padrão de screens.rpy.
init offset = 10


# ============================================================
# PALETA
# ============================================================

define COR_FUNDO_ESCURO = "#061720"
define COR_PAINEL = "#071B28E8"

define COR_MADEIRA = "#59351F"
define COR_MADEIRA_CLARA = "#81512D"

define COR_OURO = "#F1C75B"
define COR_PERGAMINHO = "#F5E9C7"

define COR_AZUL = "#174764"
define COR_AZUL_HOVER = "#236D91"

define COR_TEXTO = "#FFF7DF"
define COR_TEXTO_FRACO = "#B9C6CB"

define COR_BLOQUEADO = "#36454D"


# ============================================================
# IMAGENS DE FUNDO
# ============================================================

image bg_menu = "images/backgrounds/bg_menu.png"

image bg_mar = "images/backgrounds/bg_mar.png"

image bg_ilha = "images/backgrounds/bg_ilha.png"

image bg_final = "images/backgrounds/bg_final.png"

image bg_prisao = "images/backgrounds/bg_prisao.png"


# ============================================================
# COMPATIBILIDADE COM NOMES ANTIGOS
# ============================================================
#
# Isso permite apagar as imagens provisórias antigas
# sem quebrar algum trecho antigo ainda não executado.

image bg_ilha1_fase1 = "images/backgrounds/bg_ilha.png"
image bg_ilha2_fase1 = "images/backgrounds/bg_ilha.png"
image bg_final_fase1 = "images/backgrounds/bg_final.png"
image mapa_fundo = "images/backgrounds/bg_mar.png"


# ============================================================
# PERSONAGENS
# ============================================================

# Retratos usados automaticamente na caixa de diálogo.

image side navegador = Transform(
    "images/characters/navegador.png",
    zoom=3.0,
    nearest=True
)

image side naufrago = Transform(
    "images/characters/naufrago.png",
    zoom=3.0,
    nearest=True
)


# Retrato maior utilizado nas telas de navegação.

image retrato_navegador = Transform(
    "images/characters/navegador.png",
    zoom=3.5,
    nearest=True
)

image retrato_naufrago = Transform(
    "images/characters/naufrago.png",
    zoom=3.5,
    nearest=True
)


# ============================================================
# UI
# ============================================================

image ui_icon_mapa = Transform(
    "images/ui/icon_mapa.png",
    zoom=2.0,
    nearest=True
)

image ui_victory = Transform(
    "images/ui/victory.png",
    zoom=1.35,
    nearest=True
)

image ui_game_over = Transform(
    "images/ui/game_over.png",
    zoom=1.25,
    nearest=True
)


# ============================================================
# TRANSFORMS
# ============================================================

transform fundo_tela:

    xysize (1280, 720)

    fit "cover"


transform marca_resultado:

    xalign 0.5
    yalign 0.25

    nearest True


# ============================================================
# MAPAS
# ============================================================

init python:

    def caminho_mapa_fase(numero_fase):
        """
        Retorna o caminho esperado para o mapa da fase.

        O arquivo pode ainda não existir durante o desenvolvimento.
        """

        return (
            "images/maps/"
            "mapa_fase_"
            + str(numero_fase)
            + ".png"
        )



# ============================================================
# VISUAL GENÉRICO DOS ESTADOS
# ============================================================

label exibir_estado_visual():


    # ========================================================
    # ESTADO FINAL
    # ========================================================

    if automato.eh_final(
        configuracao_automato,
        estado_atual
    ):

        scene bg_final

        with transicao_tela


    # ========================================================
    # ARMADILHA
    # ========================================================

    elif automato.eh_armadilha(
        configuracao_automato,
        estado_atual
    ):

        scene bg_prisao

        with transicao_tela


    # ========================================================
    # ILHA NORMAL
    # ========================================================

    else:

        scene bg_ilha

        with transicao_tela


    return



# ============================================================
# MENU PRINCIPAL
# ============================================================

screen main_menu():

    tag menu


    add "bg_menu" at fundo_tela


    # Escurecimento discreto para melhorar leitura.

    add Solid("#00101955")


    frame:

        style "painel_menu"

        xalign 0.18
        yalign 0.5

        xsize 500
        ysize 650


        vbox:

            xalign 0.5
            yalign 0.5

            spacing 24


            text "ARQUIPÉLAGO\nDOS AUTÔMATOS":

                style "titulo_jogo"

                xalign 0.5

                text_align 0.5


            text "Uma aventura entre ilhas, rotas e decisões.":

                style "subtitulo_jogo"

                xalign 0.5

                text_align 0.5


            null height 20


            textbutton "Jogar":

                style "rota_button"

                xalign 0.5

                action Start()


            textbutton "Como Jogar":

                style "rota_button"

                xalign 0.5

                action ShowMenu(
                    "como_jogar"
                )


            textbutton "Sair":

                style "rota_button"

                xalign 0.5

                action config.quit_action



# ============================================================
# CONFIRMAÇÃO
# ============================================================

screen confirm(message, yes_action, no_action):

    modal True

    zorder 300


    add Solid("#000000AA")


    frame:

        style "painel_jogo"

        xalign 0.5
        yalign 0.5

        xsize 560


        vbox:

            xalign 0.5

            spacing 30


            text "[message]":

                style "texto_painel"

                xalign 0.5

                text_align 0.5


            hbox:

                xalign 0.5

                spacing 25


                textbutton "Não":

                    style "controle_button"

                    action no_action


                textbutton "Sim":

                    style "controle_button"

                    action yes_action


    key "game_menu" action no_action



# ============================================================
# DESATIVA COMPLETAMENTE O QUICK MENU
# ============================================================

screen quick_menu():

    zorder 100



# ============================================================
# ESCOLHAS DE DIÁLOGO
# ============================================================

screen choice(items):

    modal True


    vbox:

        xalign 0.5
        yalign 0.57

        spacing 12


        for i in items:

            textbutton i.caption:

                style "escolha_button"

                action i.action



# ============================================================
# MENU DE MODO
# ============================================================

screen menu_modo_jogo():

    modal True


    add "bg_menu" at fundo_tela

    add Solid("#00101966")


    frame:

        style "painel_jogo"

        xalign 0.5
        yalign 0.5

        xsize 720


        vbox:

            xalign 0.5

            spacing 25


            text "Como deseja navegar?":

                style "titulo_secao"

                xalign 0.5


            text "Cada modo utiliza o mesmo autômato, mas permite planejar as rotas de formas diferentes.":

                style "texto_painel"

                xalign 0.5
                text_align 0.5


            null height 15


            textbutton "Navegação passo a passo":

                style "rota_button"

                xalign 0.5

                action Return(
                    "navegacao"
                )


            textbutton "Planejamento de rota":

                style "rota_button"

                xalign 0.5

                action Return(
                    "rota"
                )


            null height 10


            textbutton "Voltar":

                style "controle_button"

                xalign 0.5

                action Return(
                    "__VOLTAR__"
                )



# ============================================================
# COMO JOGAR
# ============================================================

screen como_jogar():

    tag menu


    add "bg_menu" at fundo_tela

    add Solid("#00101977")


    frame:

        style "painel_jogo"

        xalign 0.5
        yalign 0.5

        xsize 1040
        ysize 640


        vbox:

            spacing 18


            text "Como Jogar":

                style "titulo_secao"

                xalign 0.5


            viewport:

                xsize 970
                ysize 490

                scrollbars "vertical"

                mousewheel True
                draggable True


                vbox:

                    xsize 900

                    spacing 28


                    text """
OBJETIVO

Navegue pelo arquipélago e encontre a Ilha do Tesouro.

Cada ilha representa um ponto da navegação e as rotas A e B determinam para qual ilha você seguirá.
""" style "texto_painel"


                    text """
NAVEGAÇÃO PASSO A PASSO

Você escolhe uma rota de cada vez.

A cada decisão, o navio segue para a próxima ilha e você pode observar o resultado antes de escolher novamente.
""" style "texto_painel"


                    text """
PLANEJAMENTO DE ROTA

Você informa uma sequência completa, como ABBAB.

O jogo executa a sequência símbolo por símbolo. A viagem pode terminar antes do fim da sequência caso você encontre a Ilha do Tesouro ou uma prisão.
""" style "texto_painel"


                    text """
REDEMOINHOS

Algumas rotas fazem o navio permanecer na mesma região. No mapa, elas são representadas por redemoinhos.
""" style "texto_painel"


                    text """
PRISÕES

Algumas fases possuem prisões. Ao entrar nelas, não existe rota de fuga e a tentativa termina.
""" style "texto_painel"


                    text """
MAPA E DICAS

Use o mapa para observar as rotas disponíveis.

O Navegador oferece dicas gerais. Alguns Náufragos também podem ajudar, dependendo do que aconteceu durante a partida e da interação com eles.
""" style "texto_painel"


            textbutton "Voltar":

                style "controle_button"

                xalign 0.5

                action ShowMenu(
                    "main_menu"
                )



# ============================================================
# SELEÇÃO DE FASE
# ============================================================

screen selecionar_fase():

    modal True


    add "bg_mar" at fundo_tela

    add Solid("#00101966")


    frame:

        style "painel_jogo"

        xalign 0.5
        yalign 0.5

        xsize 620
        ysize 660


        vbox:

            xalign 0.5

            spacing 10


            text "Escolha a fase":

                style "titulo_secao"

                xalign 0.5


            text "Novos elementos são introduzidos progressivamente.":

                style "texto_secundario"

                xalign 0.5


            null height 10


            for numero in range(1, 8):


                $ desbloqueada = (
                    numero
                    <= persistent.fase_max_desbloqueada
                )


                $ implementada = fases.fase_implementada(
                    numero
                )


                if not desbloqueada:

                    textbutton "Fase [numero]  •  Bloqueada":

                        style "fase_button"

                        xalign 0.5

                        sensitive False


                elif not implementada:

                    textbutton "Fase [numero]  •  Em desenvolvimento":

                        style "fase_button"

                        xalign 0.5

                        sensitive False


                else:

                    textbutton "Fase [numero]":

                        style "fase_button"

                        xalign 0.5

                        action Return(
                            numero
                        )


            null height 8


            textbutton "Voltar":

                style "controle_button"

                xalign 0.5

                action Return(
                    "__VOLTAR__"
                )



# ============================================================
# PASSO A PASSO
# ============================================================

screen escolha_transicao(
    nome_ilha,
    destino_a,
    destino_b
):

    modal True


    # ========================================================
    # TÍTULO
    # ========================================================

    frame:

        style "painel_jogo"

        xalign 0.5
        yalign 0.05

        xsize 470


        vbox:

            xalign 0.5

            spacing 4


            text "Fase [fase_atual]":

                style "texto_secundario"

                xalign 0.5


            text "[nome_ilha]":

                style "titulo_secao"

                xalign 0.5


    # ========================================================
    # NAVEGADOR
    # ========================================================

    frame:

        style "painel_jogo"

        xpos 70
        ypos 300

        xsize 525
        ysize 300


        hbox:

            spacing 20

            yalign 0.5


            add "retrato_navegador"


            vbox:

                xsize 250

                spacing 14


                text "Navegador":

                    style "nome_navegador"


                text "Capitão, qual das rotas devemos seguir?":

                    style "texto_painel"


    # ========================================================
    # ROTAS
    # ========================================================

    frame:

        style "painel_jogo"

        xpos 750
        ypos 300

        xsize 460
        ysize 300


        vbox:

            xalign 0.5
            yalign 0.5

            spacing 20


            text "Escolha uma rota":

                style "titulo_pequeno"

                xalign 0.5


            textbutton "A  →  [destino_a]":

                style "rota_button"

                action Return(
                    "A"
                )


            textbutton "B  →  [destino_b]":

                style "rota_button"

                action Return(
                    "B"
                )


    use controles_fase



# ============================================================
# PLANEJAMENTO DE ROTA
# ============================================================

screen entrada_rota(nome_ilha):

    modal True


    default sequencia = ""


    # Fundo próprio porque o mapa é o centro deste modo.

    add "bg_mar" at fundo_tela

    add Solid("#00101944")


    $ caminho_mapa = caminho_mapa_fase(
        fase_atual
    )


    # ========================================================
    # MAPA SEMPRE VISÍVEL
    # ========================================================

    frame:

        style "mapa_painel"

        xpos 30
        ypos 45

        xsize 780
        ysize 590


        if renpy.loadable(
            caminho_mapa
        ):

            add Transform(
                caminho_mapa,
                xysize=(750, 555),
                fit="contain"
            ):

                xalign 0.5
                yalign 0.5


        else:

            vbox:

                xalign 0.5
                yalign 0.5

                spacing 20


                add "ui_icon_mapa":

                    xalign 0.5


                text "Mapa da Fase [fase_atual]":

                    style "titulo_pequeno"

                    xalign 0.5


                text "O mapa definitivo ainda será inserido.":

                    style "texto_secundario"

                    xalign 0.5


    # ========================================================
    # PAINEL DE PLANEJAMENTO
    # ========================================================

    frame:

        style "painel_jogo"

        xpos 835
        ypos 45

        xsize 415
        ysize 590


        vbox:

            xalign 0.5

            spacing 20


            text "Planejamento de Rota":

                style "titulo_pequeno"

                xalign 0.5


            text "Fase [fase_atual]":

                style "texto_secundario"

                xalign 0.5


            text "Posição atual:\n[nome_ilha]":

                style "texto_painel"

                xalign 0.5

                text_align 0.5


            null height 5


            text "Informe uma sequência usando A e B.":

                style "texto_secundario"

                xalign 0.5

                text_align 0.5


            frame:

                background Solid("#020D14E6")

                xfill True
                ysize 62

                xpadding 18
                ypadding 10


                input:

                    value ScreenVariableInputValue(
                        "sequencia",
                        returnable=True
                    )

                    style "rota_input"

                    length 20


            text "Exemplo: ABBAB":

                style "texto_secundario"

                xalign 0.5


            textbutton "Executar rota":

                style "rota_button"

                xalign 0.5

                action Return(
                    sequencia
                )


    use controles_fase



# ============================================================
# CONTROLES DA FASE
# ============================================================

screen controles_fase():


    # No Planejamento de Rota o mapa já está permanente.

    if modo_jogo != "rota":

        button:

            style "controle_button"

            xalign 0.02
            yalign 0.97

            action Show(
                "mapa_atual"
            )


            hbox:

                spacing 8

                xalign 0.5
                yalign 0.5


                add "ui_icon_mapa"


                text "Mapa":

                    style "controle_button_text"


    hbox:

        xalign 0.98
        yalign 0.97

        spacing 10


        textbutton "Dica":

            style "controle_button"

            action Return(
                "__AJUDA__"
            )


        textbutton "Reiniciar":

            style "controle_button"

            action Return(
                "__REINICIAR__"
            )


        textbutton "Menu":

            style "controle_button"

            action Return(
                "__MENU__"
            )



# ============================================================
# MAPA ABERTO NO PASSO A PASSO
# ============================================================

screen mapa_atual():

    modal True

    zorder 250


    add Solid("#000000BB")


    $ caminho_mapa = caminho_mapa_fase(
        fase_atual
    )


    frame:

        style "mapa_painel"

        xalign 0.5
        yalign 0.5

        xsize 1080
        ysize 650


        vbox:

            xalign 0.5

            spacing 10


            text "Mapa — Fase [fase_atual]":

                style "titulo_secao"

                xalign 0.5


            fixed:

                xsize 1020
                ysize 500


                if renpy.loadable(
                    caminho_mapa
                ):

                    add Transform(
                        caminho_mapa,
                        xysize=(1020, 500),
                        fit="contain"
                    ):

                        xalign 0.5
                        yalign 0.5


                else:

                    vbox:

                        xalign 0.5
                        yalign 0.5

                        spacing 15


                        add "ui_icon_mapa":

                            xalign 0.5


                        text "Mapa ainda não inserido.":

                            style "texto_secundario"

                            xalign 0.5


            textbutton "Fechar":

                style "controle_button"

                xalign 0.5

                action Hide(
                    "mapa_atual"
                )



# ============================================================
# ESTILOS
# ============================================================


# ------------------------------------------------------------
# CAIXA DE DIÁLOGO
# ------------------------------------------------------------

style window:

    background Solid("#061720EA")


style namebox:

    background Solid("#59351FEF")


style say_label:

    color COR_OURO

    size 27

    outlines [
        (2, "#000000AA", 0, 0)
    ]


style say_dialogue:

    color COR_TEXTO

    size 27

    outlines [
        (1, "#00000088", 0, 0)
    ]



# ------------------------------------------------------------
# PAINÉIS
# ------------------------------------------------------------

style painel_jogo:

    background Solid(COR_PAINEL)

    xpadding 30
    ypadding 24


style painel_menu:

    background Solid("#061720EE")

    xpadding 34
    ypadding 30


style mapa_painel:

    background Solid("#04151FEF")

    xpadding 15
    ypadding 15



# ------------------------------------------------------------
# TEXTOS
# ------------------------------------------------------------

style titulo_jogo:

    color COR_OURO

    size 46

    bold True

    outlines [
        (3, "#000000CC", 0, 0)
    ]


style titulo_secao:

    color COR_OURO

    size 36

    bold True

    outlines [
        (2, "#000000BB", 0, 0)
    ]


style titulo_pequeno:

    color COR_OURO

    size 29

    bold True


style subtitulo_jogo:

    color COR_PERGAMINHO

    size 22


style texto_painel:

    color COR_TEXTO

    size 23

    line_spacing 5


style texto_secundario:

    color COR_TEXTO_FRACO

    size 20


style nome_navegador:

    color "#83D5FF"

    size 26

    bold True



# ------------------------------------------------------------
# BOTÕES PRINCIPAIS
# ------------------------------------------------------------

style rota_button:

    background Solid("#174764EE")

    hover_background Solid("#236D91FF")

    insensitive_background Solid("#26343BDD")

    xsize 420
    ysize 62

    xpadding 18
    ypadding 10


style rota_button_text:

    color COR_TEXTO

    hover_color COR_OURO

    insensitive_color "#78868C"

    size 25

    xalign 0.5
    yalign 0.5

    text_align 0.5

    outlines [
        (1, "#000000AA", 0, 0)
    ]



# ------------------------------------------------------------
# BOTÕES DAS FASES
# ------------------------------------------------------------

style fase_button is rota_button:

    xsize 450
    ysize 52


style fase_button_text is rota_button_text:

    size 22



# ------------------------------------------------------------
# CONTROLES PEQUENOS
# ------------------------------------------------------------

style controle_button is rota_button:

    xsize 150
    ysize 52

    xpadding 10
    ypadding 6


style controle_button_text is rota_button_text:

    size 20



# ------------------------------------------------------------
# ESCOLHAS DE DIÁLOGO
# ------------------------------------------------------------

style escolha_button is rota_button:

    xsize 600
    ysize 58


style escolha_button_text is rota_button_text:

    size 23



# ------------------------------------------------------------
# INPUT DA ROTA
# ------------------------------------------------------------

style rota_input:

    color COR_OURO

    size 30

    xalign 0.5

    text_align 0.5
define m = Character('Me', color="#c8c8ff")
define navegador = Character('Navegador', color="#c8ffc8")

default estado_atual = "q0"


label start:

    scene bg mar

    "O navio está no mar."

    m "Vejamos."

    show ch navegador

    navegador "Capitão, pra onde vamos?"

    jump ilha_1
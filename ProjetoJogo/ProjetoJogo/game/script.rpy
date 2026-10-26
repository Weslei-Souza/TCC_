define m = Character('Me', color="#1f1f89")
define navegador = Character('Navegador', color="#08eb08")

label start:

    scene bg mar
    "O navio está no mar."
    m "Vejamos."

    show ch navegador
    navegador "Capitão, pra onde vamos?"

    jump ilha_1


label ilha_1:

    scene bg ilha_1
    "Você chegou à Ilha 1."

    menu:
        "Para onde ir?"

        "Ir para a Ilha 2":
            jump ilha_2

        "Ir para a Ilha 3":
            jump ilha_3


label ilha_2:

    scene bg ilha_2
    "Você chegou à Ilha 2."

    menu:
        "Para onde ir?"

        "Voltar para a Ilha 1":
            jump ilha_1

        "Ir para a Ilha 3":
            jump ilha_3


label ilha_3:

    scene bg ilha_3
    "Você chegou à Ilha 3."

    menu:
        "Para onde ir?"

        "Voltar para a Ilha 1":
            jump ilha_1
define navegador = Character('Navegador', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")


label start:

    scene bg mar

    "O navio está no mar."

    m "Vejamos."

    show ch navegador

    navegador "Capitão, pra onde vamos!?"

    menu:

        "Seguir para a Ilha da Floresta":
            jump ilha_floresta

        "Seguir para a Ilha Rochosa":
            jump ilha_rochosa


label ilha_floresta:

    
    scene bg ilha_floresta

    "O navio chega à Ilha da Floresta."

    navegador "Chegamos à Ilha da Floresta."

    return


label ilha_rochosa:

    
    scene bg ilha_rochosa

    "O navio chega à Ilha Rochosa."

    navegador "Chegamos à Ilha Rochosa."

    return
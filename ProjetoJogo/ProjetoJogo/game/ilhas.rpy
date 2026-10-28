label ilha_1:

    $ estado_atual = "q0"

    scene bg ilha_1

    "Você chegou à Ilha 1."
    "Estado atual: [estado_atual]"

    call screen escolha_rota(
        "Ilha 1",
        "Navegador: Qual rota devemos seguir?",
        "Rota A - Ilha 2",
        "Rota B - Ilha 3"
    )

    if _return == "A":
        jump ilha_2

    elif _return == "B":
        jump ilha_3

label ilha_2:

    $ estado_atual = "q1"

    scene bg ilha_2

    "Você chegou à Ilha 2."
    "Estado atual: [estado_atual]"

    call screen escolha_rota(
        "Ilha 2",
        "Navegador: Temos duas rotas novamente.",
        "Rota A - Ilha 1",
        "Rota B - Ilha 3"
    )

    if _return == "A":
        jump ilha_1

    elif _return == "B":
        jump ilha_3

label ilha_3:

    $ estado_atual = "q2"

    scene bg ilha_3

    "Você chegou à Ilha 3."
    "Estado atual: [estado_atual]"

    call screen escolha_rota(
        "Ilha 3",
        "Navegador: Precisamos decidir.",
        "Rota A - Ilha 1",
        "Rota B - Ilha Final"
    )

    if _return == "A":
        jump ilha_1

    elif _return == "B":
        jump ilha_final

label ilha_final:

    $ estado_atual = "qf"

    scene bg ilha_final

    "Você chegou à Ilha Final."
    "Estado atual: [estado_atual]"

    "O percurso foi concluído."

    return
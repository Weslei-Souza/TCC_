label exibir_ilha_atual:

    if estado_atual == "q0":

        scene bg ilha_1

        "Você está na Ilha 1."
        "Estado atual: q0."


    elif estado_atual == "q1":

        scene bg ilha_2

        "Você está na Ilha 2."
        "Estado atual: q1."


    elif estado_atual == "q2":

        scene bg ilha_3

        "Você está na Ilha 3."
        "Estado atual: q2."


    elif estado_atual == "qf":

        scene bg ilha_final

        "Você chegou à Ilha Final."
        "Estado atual: qf."

    return
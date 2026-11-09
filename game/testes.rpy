# ============================================================
# TESTES AUTOMATIZADOS DO SISTEMA
# ============================================================

init python:

    from logica import testes_sistema


label executar_testes_sistema:


    # ========================================================
    # EXECUTA A BATERIA
    # ========================================================

    $ resultado_testes = testes_sistema.executar_todos_testes()


    $ relatorio_testes = testes_sistema.formatar_relatorio(
        resultado_testes
    )


    # ========================================================
    # SALVA NO LOG
    # ========================================================

    python:

        for linha in relatorio_testes.splitlines():

            renpy.log(
                linha
            )


    # ========================================================
    # RESUMO
    # ========================================================

    "Testes automatizados concluídos."


    "Aprovados: [resultado_testes['aprovados']]"


    "Falhas: [len(resultado_testes['falhas'])]"


    # ========================================================
    # MOSTRAR AS FALHAS NA TELA
    # ========================================================

    if resultado_testes["falhas"]:

        "Foram encontradas falhas:"


        python:

            for falha in resultado_testes["falhas"]:

                renpy.say(
                    None,
                    falha
                )


    else:

        "Nenhuma falha automática foi encontrada."


    # ========================================================
    # DIAGNÓSTICOS
    # ========================================================

    if resultado_testes["diagnosticos"]:

        "Diagnósticos do sistema:"


        python:

            for diagnostico in resultado_testes["diagnosticos"]:

                renpy.say(
                    None,
                    diagnostico
                )


    return
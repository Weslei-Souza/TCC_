# ============================================================
# TESTES AUTOMATIZADOS DO SISTEMA
# ============================================================

init python:

    from logica import testes_sistema



label executar_testes_sistema:

    $ resultado_testes = testes_sistema.executar_todos_testes()

    $ relatorio_testes = testes_sistema.formatar_relatorio(
        resultado_testes
    )


    # ========================================================
    # REGISTRA O RELATÓRIO NO LOG
    # ========================================================

    python:

        for linha in relatorio_testes.splitlines():

            renpy.log(
                linha
            )


    # ========================================================
    # RESULTADO GERAL
    # ========================================================

    "Testes automatizados concluídos."

    "Aprovados: [resultado_testes['aprovados']]"


    if resultado_testes["falhas"]:

        "Foram encontradas [len(resultado_testes['falhas'])] falhas."


        python:

            for falha in resultado_testes["falhas"]:

                renpy.say(
                    None,
                    falha
                )


    else:

        "Nenhuma falha automática foi encontrada."


    # ========================================================
    # DIAGNÓSTICOS DO FUZZY
    # ========================================================

    if resultado_testes["diagnosticos"]:

        "Diagnósticos do sistema fuzzy:"


        $ diagnostico_necessidade = resultado_testes["diagnosticos"][0]

        $ diagnostico_disposicao = resultado_testes["diagnosticos"][1]


        "[diagnostico_necessidade]"

        "[diagnostico_disposicao]"


    return
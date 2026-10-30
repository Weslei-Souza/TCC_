# 
# AÇÕES GERAIS DO JOGO



# DICAS GENÉRICAS


# Estas dicas podem ser utilizadas em qualquer fase.

define DICAS_GERAIS = [

    "Observe o mapa antes de escolher uma rota.",

    "Cada letra representa uma transição entre dois estados.",

    "Acompanhe o estado em que você está antes de decidir o próximo caminho.",
]


#############
# REINICIAR FASE


label reiniciar_fase:

    # Registra o reinício.
    $ numero_resets += 1


    # Volta ao estado inicial definido pelo autômato
    # correspondente à fase atual.

    $ estado_atual = automato.estado_inicial(
        configuracao_automato
    )


    # O percurso atual começa novamente no estado inicial.
    $ historico_estados = [estado_atual]


    navegador "Vamos recomeçar o percurso, capitão."


    return
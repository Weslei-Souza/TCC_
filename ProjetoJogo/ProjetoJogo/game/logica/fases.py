"""
Configuração geral das fases do jogo.

Este módulo contém apenas informações sobre
as fases disponíveis.

A lógica dos autômatos será implementada
separadamente.
"""


FASES = {
#estados basicos
    1: {
        "nome": "Primeiros Estados",
        "implementada": True
    },
#mais do mesmo, um pouco mais dificil
    2: {
        "nome": "Novas Rotas",
        "implementada": False
    },
#diferentes rotas pra vitoria
    3: {
        "nome": "Caminhos Alternativos",
        "implementada": False
    },
#loops
    4: {
        "nome": "O Redemoinho",
        "implementada": False
    },
#fase com tudo meio junto
    5: {
        "nome": "Rotas Complexas",
        "implementada": False
    },
#estado de morte/armadilha
    6: {
        "nome": "A Prisão",
        "implementada": False
    },
#fase dificil
    7: {
        "nome": "Desafio Final",
        "implementada": False
    }

}


def obter_fase(numero):
    """
    Retorna os dados de uma fase.
    """

    return FASES.get(numero)
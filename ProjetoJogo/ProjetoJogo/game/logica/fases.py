"""
Configuração geral das fases do jogo.
"""
from logica.automatos import fase_1

FASES = {

    1: {
        "nome": "Primeiros Estados",
        "implementada": True,
        "automato": fase_1.CONFIGURACAO,
    },

    2: {
        "nome": "Novas Rotas",
        "implementada": False,
        "automato": None,
    },

    3: {
        "nome": "Caminhos Alternativos",
        "implementada": False,
        "automato": None,
    },

    4: {
        "nome": "O Redemoinho",
        "implementada": False,
        "automato": None,
    },

    5: {
        "nome": "Rotas Complexas",
        "implementada": False,
        "automato": None,
    },

    6: {
        "nome": "A Prisão",
        "implementada": False,
        "automato": None,
    },

    7: {
        "nome": "Desafio Final",
        "implementada": False,
        "automato": None,
    }

}


def obter_fase(numero):
    return FASES.get(numero)


def obter_automato(numero):
    fase = obter_fase(numero)

    if fase is None:
        return None

    return fase.get("automato")
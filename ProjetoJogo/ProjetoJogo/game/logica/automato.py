ESTADO_INICIAL = "q0"

ESTADOS_FINAIS = {"qf"}


NOMES_ESTADOS = {
    "q0": "Ilha 1",
    "q1": "Ilha 2",
    "q2": "Ilha 3",
    "qf": "Ilha Final",
}


TRANSICOES = {
    "q0": {
        "A": "q1",
        "B": "q2",
    },

    "q1": {
        "A": "q0",
        "B": "q2",
    },

    "q2": {
        "A": "q0",
        "B": "qf",
    },

    "qf": {}
}


def nome_estado(estado):
    """Retorna o nome da ilha associada ao estado."""
    return NOMES_ESTADOS.get(estado, "Estado desconhecido")


def eh_final(estado):
    """Informa se o estado recebido é um estado final."""
    return estado in ESTADOS_FINAIS


def transicao(estado_atual, simbolo):
    """
    Executa uma transição a partir do estado atual.

    Retorna o próximo estado ou None caso
    a transição não exista.
    """

    simbolo = simbolo.strip().upper()

    return TRANSICOES.get(estado_atual, {}).get(simbolo)


def processar_sequencia(estado_inicial, sequencia):
    """
    Processa uma sequência inteira, como AAB.

    Retorna:
    - estado final alcançado;
    - lista dos estados percorridos;
    - possível mensagem de erro.
    """

    estado = estado_inicial
    sequencia = sequencia.replace(" ", "").upper()

    caminho = [estado]

    if not sequencia:
        return estado, caminho, "Nenhuma rota foi informada."

    for simbolo in sequencia:

        if simbolo not in ("A", "B"):

            return (
                estado,
                caminho,
                f"Símbolo inválido: {simbolo}. Use apenas A ou B."
            )

        proximo_estado = transicao(estado, simbolo)

        if proximo_estado is None:

            return (
                estado,
                caminho,
                f"Não existe uma rota {simbolo} a partir de {nome_estado(estado)}."
            )

        estado = proximo_estado
        caminho.append(estado)

    "DEBUG - Histórico: [historico_estados]"
    "DEBUG - Estados repetidos: [estados_repetidos]"
    "DEBUG - Retornos: [quantidade_retornos]"

    return estado, caminho, None
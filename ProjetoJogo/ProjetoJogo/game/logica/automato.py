"""
Motor genérico para processamento de autômatos.
"""


def estado_inicial(configuracao):
    """
    Retorna o estado inicial do autômato.
    """

    return configuracao["estado_inicial"]



def nome_estado(configuracao, estado):
    """
    Retorna o nome associado a um estado.
    """

    return configuracao["nomes_estados"].get(
        estado,
        "Estado desconhecido"
    )



def eh_final(configuracao, estado):
    """
    Verifica se um estado pertence ao conjunto
    de estados finais.
    """

    return estado in configuracao["estados_finais"]



def transicao(configuracao, estado_atual, simbolo):
    """
    Executa uma transição

    Recebe:
    - configuração do autômato
    - estado atual
    - símbolo da entrada

    Retorna o próximo estado ou None caso
    a transição não exista.
    """

    simbolo = simbolo.strip().upper()

    transicoes = configuracao["transicoes"]

    return transicoes.get(
        estado_atual,
        {}
    ).get(simbolo)



def processar_sequencia(
    configuracao,
    estado_inicial,
    sequencia
):
    """
    Processa uma sequência completa de símbolos
    
    Retorna:

    - estado final alcançado;
    - lista de estados percorridos;
    - possível mensagem de erro.
    """

    estado = estado_inicial

    sequencia = sequencia.replace(
        " ",
        ""
    ).upper()

    caminho = [estado]


    if not sequencia:

        return (
            estado,
            caminho,
            "Nenhuma rota foi informada."
        )


    for simbolo in sequencia:


        if simbolo not in ("A", "B"):

            return (
                estado,
                caminho,
                f"Símbolo inválido: {simbolo}. Use apenas A ou B."
            )


        proximo_estado = transicao(
            configuracao,
            estado,
            simbolo
        )


        if proximo_estado is None:

            return (
                estado,
                caminho,
                f"Não existe uma rota {simbolo} a partir de "
                f"{nome_estado(configuracao, estado)}."
            )


        estado = proximo_estado

        caminho.append(estado)


    return (
        estado,
        caminho,
        None
    )
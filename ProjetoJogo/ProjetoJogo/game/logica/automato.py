"""
Motor genérico para processamento de autômatos.
"""


# ============================================================
# ESTADO INICIAL
# ============================================================

def estado_inicial(configuracao):

    return configuracao["estado_inicial"]


# ============================================================
# NOME DO ESTADO
# ============================================================

def nome_estado(configuracao, estado):

    return configuracao["nomes_estados"].get(
        estado,
        "Estado desconhecido"
    )

# ============================================================
# NOMES DE UM PERCURSO
# ============================================================

def nomes_caminho(configuracao, caminho):
    """
    Converte uma sequência de identificadores internos
    de estados para seus nomes apresentados ao jogador.

    Exemplo:

    ["q0", "q2", "qf"]

    torna-se:

    ["Ilha 1", "Ilha 3", "Ilha Final"]
    """

    return [
        nome_estado(
            configuracao,
            estado
        )
        for estado in caminho
    ]

# ============================================================
# ESTADO FINAL
# ============================================================

def eh_final(configuracao, estado):

    return estado in configuracao["estados_finais"]


# ============================================================
# ALFABETO
# ============================================================

def obter_alfabeto(configuracao):

    return configuracao["alfabeto"]


# ============================================================
# TRANSIÇÃO
# ============================================================

def transicao(configuracao, estado_atual, simbolo):
    """
    Executa uma transição.

    Retorna o próximo estado associado ao símbolo.
    """

    simbolo = simbolo.strip().upper()

    transicoes = configuracao["transicoes"]

    return transicoes.get(
        estado_atual,
        {}
    ).get(simbolo)


# ============================================================
# VALIDAÇÃO DO AUTÔMATO DETERMINÍSTICO
# ============================================================

def validar_determinismo(configuracao):
    """
    Verifica se cada estado possui exatamente um destino
    definido para cada símbolo do alfabeto.

    Como as transições são armazenadas em dicionários,
    um mesmo símbolo não pode possuir dois destinos
    simultaneamente.

    Portanto, é necessário verificar principalmente:

    - se todos os estados possuem todas as transições;
    - se todos os destinos definidos existem.
    """

    alfabeto = configuracao["alfabeto"]

    estados = configuracao["nomes_estados"]

    transicoes = configuracao["transicoes"]


    for estado in estados:

        if estado not in transicoes:

            return False


        for simbolo in alfabeto:

            destino = transicoes[estado].get(simbolo)


            if destino is None:

                return False


            if destino not in estados:

                return False


    return True


# ============================================================
# PROCESSAMENTO DE SEQUÊNCIA
# ============================================================

def processar_sequencia(
    configuracao,
    estado_inicial,
    sequencia
):
    """
    Processa uma sequência completa de símbolos.

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


    alfabeto = obter_alfabeto(
        configuracao
    )


    for simbolo in sequencia:


        if simbolo not in alfabeto:

            simbolos_validos = " ou ".join(
                sorted(alfabeto)
            )

            return (
                estado,
                caminho,
                f"Símbolo inválido: {simbolo}. "
                f"Use apenas {simbolos_validos}."
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
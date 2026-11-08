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
# ESTADO INICIAL
# ============================================================

def eh_inicial(configuracao, estado):
    """
    Verifica se o estado informado é o estado inicial
    da fase atual.
    """

    return estado == configuracao["estado_inicial"]


# ============================================================
# ESTADO DE ARMADILHA
# ============================================================

def eh_armadilha(configuracao, estado):
    """
    Verifica se o estado atual está marcado como armadilha.

    Fases sem armadilhas possuem um conjunto vazio.
    """

    estados_armadilha = configuracao.get(
        "estados_armadilha",
        set()
    )

    return estado in estados_armadilha


# ============================================================
# ESTADO INTERMEDIÁRIO
# ============================================================

def eh_intermediario(configuracao, estado):
    """
    Um estado intermediário:

    - não é inicial;
    - não é final;
    - não é armadilha.

    Esses serão os estados elegíveis para encontros
    aleatórios com NPC.
    """

    return (
        not eh_inicial(configuracao, estado)
        and not eh_final(configuracao, estado)
        and not eh_armadilha(configuracao, estado)
    )

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
                f"Use apenas {simbolos_validos}. "
                f"Você permanece em "
                f"{nome_estado(configuracao, estado)}."
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
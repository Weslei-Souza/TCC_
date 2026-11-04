"""
Funções relacionadas ao estado interno dos NPCs.

A variável utilizada no jogo é chamada de Disposição do NPC.

No texto acadêmico:
Disposição Afetiva.

A disposição utiliza uma escala contínua de 0 a 100.
"""


# ============================================================
# LIMITES DA DISPOSIÇÃO
# ============================================================

DISPOSICAO_MINIMA = 0.0
DISPOSICAO_MAXIMA = 100.0


# ============================================================
# IMPACTOS DAS INTERAÇÕES
# ============================================================

# Estes valores são parâmetros iniciais de projeto.
#
# Eles representam a intensidade relativa das escolhas
# realizadas pelo jogador.
#
# Poderão ser ajustados posteriormente por meio dos testes
# de simulação do sistema.

IMPACTOS_INTERACOES = {

    "ajudar": 20,

    "nao_ajudar": -10,

    "jogar_ao_mar": -40,

    "despedir_educadamente": 10,

    "insultar": -20,

    "ignorar": -5,
}


# ============================================================
# LIMITAR DISPOSIÇÃO
# ============================================================

def limitar_disposicao(valor):
    """
    Garante que a Disposição permaneça entre 0 e 100.
    """

    return max(
        DISPOSICAO_MINIMA,
        min(
            float(valor),
            DISPOSICAO_MAXIMA
        )
    )


# ============================================================
# OBTER IMPACTO DE UMA AÇÃO
# ============================================================

def obter_impacto(acao):
    """
    Retorna o impacto associado a uma interação.

    Caso a ação não exista, gera um erro para facilitar
    a identificação de problemas durante o desenvolvimento.
    """

    if acao not in IMPACTOS_INTERACOES:

        raise ValueError(
            f"Interação de NPC desconhecida: {acao}"
        )


    return IMPACTOS_INTERACOES[acao]


# ============================================================
# APLICAR IMPACTO DIRETAMENTE
# ============================================================

def aplicar_impacto(disposicao_atual, impacto):
    """
    Aplica um impacto numérico à disposição atual.
    """

    nova_disposicao = (
        disposicao_atual + impacto
    )


    return limitar_disposicao(
        nova_disposicao
    )


# ============================================================
# APLICAR INTERAÇÃO
# ============================================================

def aplicar_interacao(disposicao_atual, acao):
    """
    Aplica uma interação previamente cadastrada.

    Retorna:

    - nova disposição;
    - impacto utilizado.
    """

    impacto = obter_impacto(
        acao
    )


    nova_disposicao = aplicar_impacto(
        disposicao_atual,
        impacto
    )


    return nova_disposicao, impacto


# ============================================================
# CLASSIFICAÇÃO NARRATIVA
# ============================================================

def classificar_disposicao_narrativa(valor):
    """
    Classificação utilizada apenas para a percepção
    narrativa inicial do Navegador.

    NÃO representa a fuzzificação.

    0 a 33   -> hostil
    34 a 66  -> neutro
    67 a 100 -> amigável
    """

    valor = limitar_disposicao(
        valor
    )


    if valor <= 33:

        return "hostil"


    if valor <= 66:

        return "neutro"


    return "amigavel"
"""
Funções relacionadas ao estado interno dos NPCs.

A variável utilizada no jogo é chamada de Disposição do NPC.

No texto acadêmico, ela será tratada como
Disposição Afetiva.

A disposição utiliza uma escala contínua de 0 a 100.
"""


# ============================================================
# LIMITES DA DISPOSIÇÃO
# ============================================================

DISPOSICAO_MINIMA = 0.0
DISPOSICAO_MAXIMA = 100.0


# ============================================================
# LIMITAR DISPOSIÇÃO
# ============================================================

def limitar_disposicao(valor):
    """
    Garante que a Disposição do NPC permaneça
    dentro do intervalo de 0 a 100.

    Exemplos:

    120 -> 100
    -15 -> 0
    63 -> 63
    """

    return max(
        DISPOSICAO_MINIMA,
        min(
            float(valor),
            DISPOSICAO_MAXIMA
        )
    )


# ============================================================
# APLICAR IMPACTO DE UMA INTERAÇÃO
# ============================================================

def aplicar_impacto(disposicao_atual, impacto):
    """
    Atualiza a Disposição do NPC a partir do impacto
    produzido por uma escolha do jogador.

    O impacto pode ser:

    positivo -> aumenta a disposição;
    negativo -> diminui a disposição;
    zero     -> mantém a disposição.

    O resultado permanece limitado entre 0 e 100.
    """

    nova_disposicao = (
        disposicao_atual + impacto
    )

    return limitar_disposicao(
        nova_disposicao
    )


# ============================================================
# CLASSIFICAÇÃO NARRATIVA
# ============================================================

def classificar_disposicao_narrativa(valor):
    """
    Retorna uma classificação simples utilizada apenas
    para a percepção narrativa do Navegador.

    IMPORTANTE:
    esta classificação NÃO representa ainda
    a fuzzificação da Disposição Afetiva.

    A fuzzificação será implementada posteriormente.

    As três faixas atuais dividem a escala 0-100
    aproximadamente em três partes.
    """

    valor = limitar_disposicao(
        valor
    )


    if valor <= 33:

        return "hostil"


    if valor <= 66:

        return "neutro"


    return "amigavel"
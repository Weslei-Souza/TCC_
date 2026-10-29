"""
Funções responsáveis pela análise da navegação do jogador.

Este módulo não armazena diretamente o estado da partida.
Ele recebe dados do Ren'Py, processa essas informações
e devolve os resultados.
"""


def registrar_percurso(historico_atual, novos_estados):
    """
    Registra novos estados visitados pelo jogador.

    e retorna:
    - histórico atualizado;
    -quantidade de estados repetidos encontrados;
    - quantidade de retornos imediatos (Loops ou
    quando vai q0>q1>q0).
    """

    historico = list(historico_atual)

    repeticoes = 0
    retornos = 0

    for estado in novos_estados:

        # Verifica se o estado já havia sido visitado.
        if estado in historico:
            repeticoes += 1

        # Verifica retorno ao estado anterior.
        if len(historico) >= 2:

            if estado == historico[-2]:
                retornos += 1

        historico.append(estado)

    return historico, repeticoes, retornos
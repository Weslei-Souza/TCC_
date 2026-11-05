"""
Bateria automatizada de testes do núcleo lógico do jogo.

Este módulo testa:

- métricas do jogador;
- Necessidade de Assistência;
- Disposição do NPC;
- impactos das interações;
- sistema fuzzy;
- autômato da Fase 1.

Os testes não modificam o estado da partida.
"""


import math

from logica import jogador
from logica import npc
from logica import fuzzy
from logica import automato

from logica.automatos import fase_1


# ============================================================
# UTILITÁRIOS
# ============================================================

def aproximadamente_igual(a, b, tolerancia=0.02):

    return abs(a - b) <= tolerancia


def executar_todos_testes():

    aprovados = 0
    falhas = []
    diagnosticos = []


    def verificar(condicao, nome, detalhe=""):

        nonlocal aprovados

        if condicao:

            aprovados += 1

        else:

            mensagem = nome

            if detalhe:
                mensagem += f" -> {detalhe}"

            falhas.append(mensagem)


    # ========================================================
    # 1. NORMALIZAÇÃO
    # ========================================================

    verificar(
        jogador.normalizar_metrica(0, 3) == 0.0,
        "Normalização: zero"
    )

    verificar(
        aproximadamente_igual(
            jogador.normalizar_metrica(1, 3),
            1 / 3
        ),
        "Normalização: 1 de 3"
    )

    verificar(
        jogador.normalizar_metrica(3, 3) == 1.0,
        "Normalização: limite"
    )

    verificar(
        jogador.normalizar_metrica(10, 3) == 1.0,
        "Normalização: saturação"
    )

    verificar(
        jogador.normalizar_metrica(1, None) is None,
        "Normalização: métrica não aplicável"
    )


    # ========================================================
    # 2. NECESSIDADE DE ASSISTÊNCIA
    # ========================================================

    limites_fase_1 = {

        "reinicios": 3,
        "dicas_pedidas": 3,
        "estados_repetidos": 3,
        "armadilhas": None,
    }


    necessidade = jogador.calcular_necessidade_assistencia(
        0, 0, 0, 0,
        limites_fase_1
    )

    verificar(
        necessidade == 0.0,
        "Necessidade: tudo zero"
    )


    necessidade = jogador.calcular_necessidade_assistencia(
        0, 1, 0, 0,
        limites_fase_1
    )

    verificar(
        aproximadamente_igual(
            necessidade,
            11.11
        ),
        "Necessidade: uma dica",
        f"resultado={necessidade}"
    )


    necessidade = jogador.calcular_necessidade_assistencia(
        1, 1, 1, 0,
        limites_fase_1
    )

    verificar(
        aproximadamente_igual(
            necessidade,
            33.33
        ),
        "Necessidade: uma ocorrência de cada",
        f"resultado={necessidade}"
    )


    necessidade = jogador.calcular_necessidade_assistencia(
        3, 3, 3, 0,
        limites_fase_1
    )

    verificar(
        necessidade == 100.0,
        "Necessidade: saturação de todas as métricas",
        f"resultado={necessidade}"
    )


    # ========================================================
    # 3. NECESSIDADE NUNCA DEVE DIMINUIR
    # ========================================================

    metricas = [
        "reinicios",
        "dicas",
        "repeticoes",
    ]


    for indice, metrica in enumerate(metricas):

        anterior = -1

        monotona = True


        for valor in range(0, 11):

            valores = [0, 0, 0]

            valores[indice] = valor


            atual = jogador.calcular_necessidade_assistencia(
                valores[0],
                valores[1],
                valores[2],
                0,
                limites_fase_1
            )


            if atual < anterior:

                monotona = False

                break


            anterior = atual


        verificar(
            monotona,
            f"Necessidade monotônica: {metrica}"
        )


    # ========================================================
    # 4. HISTÓRICO E ESTADOS REPETIDOS
    # ========================================================

    historico, repeticoes = jogador.registrar_percurso(
        ["q0", "q1"],
        ["q0", "q2", "q0"]
    )


    verificar(
        repeticoes == 2,
        "Contagem de estados repetidos",
        f"resultado={repeticoes}"
    )


    verificar(
        historico == [
            "q0",
            "q1",
            "q0",
            "q2",
            "q0"
        ],
        "Atualização do histórico de estados"
    )


    # ========================================================
    # 5. DISPOSIÇÃO DO NPC
    # ========================================================

    verificar(
        npc.limitar_disposicao(-20) == 0,
        "Disposição: limite inferior"
    )

    verificar(
        npc.limitar_disposicao(120) == 100,
        "Disposição: limite superior"
    )

    verificar(
        npc.aplicar_interacao(
            40,
            "ajudar"
        )[0] == 60,
        "NPC: ajudar +20"
    )

    verificar(
        npc.aplicar_interacao(
            40,
            "nao_ajudar"
        )[0] == 30,
        "NPC: não ajudar -10"
    )

    verificar(
        npc.aplicar_interacao(
            30,
            "jogar_ao_mar"
        )[0] == 0,
        "NPC: jogar ao mar com saturação"
    )

    verificar(
        npc.aplicar_interacao(
            40,
            "conversar_educadamente"
        )[0] == 50,
        "NPC: conversar educadamente +10"
    )

    verificar(
        npc.aplicar_interacao(
            10,
            "insultar"
        )[0] == 0,
        "NPC: insultar com saturação"
    )

    verificar(
        npc.aplicar_interacao(
            40,
            "ignorar"
        )[0] == 35,
        "NPC: ignorar -5"
    )


    # ========================================================
    # 6. CLASSIFICAÇÃO NARRATIVA
    # ========================================================

    verificar(
        npc.classificar_disposicao_narrativa(0)
        == "hostil",
        "Classificação: 0 hostil"
    )

    verificar(
        npc.classificar_disposicao_narrativa(33)
        == "hostil",
        "Classificação: 33 hostil"
    )

    verificar(
        npc.classificar_disposicao_narrativa(34)
        == "neutro",
        "Classificação: 34 neutro"
    )

    verificar(
        npc.classificar_disposicao_narrativa(66)
        == "neutro",
        "Classificação: 66 neutro"
    )

    verificar(
        npc.classificar_disposicao_narrativa(67)
        == "amigavel",
        "Classificação: 67 amigável"
    )

    verificar(
        npc.classificar_disposicao_narrativa(100)
        == "amigavel",
        "Classificação: 100 amigável"
    )


    # ========================================================
    # 7. FUNÇÕES DE PERTINÊNCIA
    # ========================================================

    pertinencias_validas = True
    cobertura_valida = True


    for valor in range(0, 101):

        grupos = [

            fuzzy.pertinencia_necessidade(
                valor
            ),

            fuzzy.pertinencia_disposicao(
                valor
            ),

            fuzzy.pertinencia_saida(
                valor
            ),
        ]


        for grupo in grupos:

            for grau in grupo.values():

                if grau < 0 or grau > 1:

                    pertinencias_validas = False


            if max(grupo.values()) <= 0:

                cobertura_valida = False


    verificar(
        pertinencias_validas,
        "Fuzzy: pertinências sempre entre 0 e 1"
    )

    verificar(
        cobertura_valida,
        "Fuzzy: universo inteiro possui cobertura"
    )


    # ========================================================
    # 8. CASOS DE REFERÊNCIA DO FUZZY ATUAL
    # ========================================================

    casos_fuzzy = [

        (0, 0, "nenhuma"),

        (0, 100, "generica"),

        (50, 0, "nenhuma"),

        (50, 50, "generica"),

        (50, 100, "intermediaria"),

        (100, 0, "generica"),

        (100, 50, "intermediaria"),

        (100, 100, "especifica"),
    ]


    for necessidade, disposicao, esperado in casos_fuzzy:

        resultado = fuzzy.calcular_assistencia(
            necessidade,
            disposicao
        )


        verificar(
            resultado["categoria"] == esperado,
            (
                "Fuzzy referência: "
                f"N={necessidade}, D={disposicao}"
            ),
            (
                f"esperado={esperado}, "
                f"obtido={resultado['categoria']}"
            )
        )


    # ========================================================
    # 9. TESTE EM MASSA DO FUZZY
    # ========================================================

    categorias_validas = {

        "nenhuma",
        "generica",
        "intermediaria",
        "especifica",
    }


    grade_valida = True

    primeiro_erro_grade = None


    # 101 x 101 = 10.201 combinações.

    for necessidade in range(0, 101):

        for disposicao in range(0, 101):

            resultado = fuzzy.calcular_assistencia(
                necessidade,
                disposicao
            )


            valor = resultado["valor"]

            categoria = resultado["categoria"]


            if (
                not math.isfinite(valor)
                or valor < 0
                or valor > 100
                or categoria not in categorias_validas
            ):

                grade_valida = False

                primeiro_erro_grade = (
                    necessidade,
                    disposicao,
                    resultado
                )

                break


        if not grade_valida:
            break


    verificar(
        grade_valida,
        "Fuzzy: grade completa 101x101 válida",
        str(primeiro_erro_grade)
        if primeiro_erro_grade
        else ""
    )


    # ========================================================
    # 10. DIAGNÓSTICO DE MONOTONICIDADE DO FUZZY
    # ========================================================

    # Este bloco é diagnóstico, não reprova o teste.
    #
    # Queremos descobrir se aumentar Necessidade ou
    # Disposição em algum ponto reduz numericamente a saída.

    quedas_por_necessidade = 0
    quedas_por_disposicao = 0


    for disposicao in range(0, 101):

        anterior = None

        for necessidade in range(0, 101):

            atual = fuzzy.calcular_assistencia(
                necessidade,
                disposicao
            )["valor"]


            if (
                anterior is not None
                and atual < anterior
            ):

                quedas_por_necessidade += 1


            anterior = atual


    for necessidade in range(0, 101):

        anterior = None

        for disposicao in range(0, 101):

            atual = fuzzy.calcular_assistencia(
                necessidade,
                disposicao
            )["valor"]


            if (
                anterior is not None
                and atual < anterior
            ):

                quedas_por_disposicao += 1


            anterior = atual


    diagnosticos.append(
        (
            "Quedas ao aumentar Necessidade: "
            f"{quedas_por_necessidade}"
        )
    )

    diagnosticos.append(
        (
            "Quedas ao aumentar Disposição: "
            f"{quedas_por_disposicao}"
        )
    )


    # ========================================================
    # 11. AUTÔMATO DA FASE 1
    # ========================================================

    configuracao = fase_1.CONFIGURACAO


    # --------------------------------------------------------
    # VALIDAÇÃO DO AUTÔMATO
    # --------------------------------------------------------

    verificar(
        automato.validar_determinismo(
            configuracao
        ),
        "Autômato Fase 1: determinístico e completo"
    )


    # --------------------------------------------------------
    # PERCURSO BB
    # --------------------------------------------------------

    estado, caminho, erro = automato.processar_sequencia(
        configuracao,
        "q0",
        "BB"
    )


    caminho_legivel = automato.nomes_caminho(
        configuracao,
        caminho
    )


    verificar(
        estado == "qf"
        and erro is None,
        "Autômato Fase 1: BB chega ao final",
        (
            f"estado={automato.nome_estado(configuracao, estado)}, "
            f"caminho={caminho_legivel}, "
            f"erro={erro}"
        )
    )


    # --------------------------------------------------------
    # PERCURSO ABB
    # --------------------------------------------------------

    estado, caminho, erro = automato.processar_sequencia(
        configuracao,
        "q0",
        "ABB"
    )


    caminho_legivel = automato.nomes_caminho(
        configuracao,
        caminho
    )


    verificar(
        estado == "qf"
        and erro is None,
        "Autômato Fase 1: ABB chega ao final",
        (
            f"estado={automato.nome_estado(configuracao, estado)}, "
            f"caminho={caminho_legivel}, "
            f"erro={erro}"
        )
    )


    # --------------------------------------------------------
    # SÍMBOLO INVÁLIDO
    # --------------------------------------------------------

    estado, caminho, erro = automato.processar_sequencia(
        configuracao,
        "q0",
        "C"
    )


    verificar(
        erro is not None,
        "Autômato Fase 1: símbolo inválido detectado",
        (
            f"estado={automato.nome_estado(configuracao, estado)}, "
            f"erro={erro}"
        )
    )

    # ========================================================
    # RESULTADO
    # ========================================================

    return {

        "aprovados": aprovados,

        "falhas": falhas,

        "diagnosticos": diagnosticos,
    }


# ============================================================
# FORMATAR RELATÓRIO
# ============================================================

def formatar_relatorio(resultado):

    linhas = []

    linhas.append(
        "========================================"
    )

    linhas.append(
        "RELATÓRIO DE TESTES DO SISTEMA"
    )

    linhas.append(
        "========================================"
    )


    linhas.append(
        f"Testes aprovados: {resultado['aprovados']}"
    )

    linhas.append(
        f"Falhas: {len(resultado['falhas'])}"
    )


    if resultado["falhas"]:

        linhas.append("")

        linhas.append("FALHAS:")

        for falha in resultado["falhas"]:

            linhas.append(
                f"- {falha}"
            )


    linhas.append("")

    linhas.append("DIAGNÓSTICOS:")


    for diagnostico in resultado["diagnosticos"]:

        linhas.append(
            f"- {diagnostico}"
        )


    linhas.append(
        "========================================"
    )


    return "\n".join(
        linhas
    )
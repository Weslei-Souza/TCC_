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

from copy import deepcopy

from logica import fases

from logica.automatos import (
    fase_1,
    fase_2,
    fase_3,
    fase_4,
    fase_5,
    fase_6,
    fase_7,
)

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

    diagnosticos.append(
        (
            "Fases registradas: "
            f"{fases.fases_implementadas()}"
        )
    )

    # ========================================================
    # 10.1 DIAGNÓSTICO DE REGRESSÃO DAS CATEGORIAS
    # ========================================================

    ordem_categorias = {
        "nenhuma": 0,
        "generica": 1,
        "intermediaria": 2,
        "especifica": 3,
    }


    regressoes_categoria_necessidade = 0
    regressoes_categoria_disposicao = 0


    # --------------------------------------------------------
    # AUMENTANDO A NECESSIDADE
    # --------------------------------------------------------

    for disposicao in range(0, 101):

        categoria_anterior = None


        for necessidade in range(0, 101):

            resultado = fuzzy.calcular_assistencia(
                necessidade,
                disposicao
            )

            categoria_atual = resultado[
                "categoria"
            ]


            if categoria_anterior is not None:

                if (
                    ordem_categorias[categoria_atual]
                    <
                    ordem_categorias[categoria_anterior]
                ):

                    regressoes_categoria_necessidade += 1


            categoria_anterior = categoria_atual


    # --------------------------------------------------------
    # AUMENTANDO A DISPOSIÇÃO
    # --------------------------------------------------------

    for necessidade in range(0, 101):

        categoria_anterior = None


        for disposicao in range(0, 101):

            resultado = fuzzy.calcular_assistencia(
                necessidade,
                disposicao
            )

            categoria_atual = resultado[
                "categoria"
            ]


            if categoria_anterior is not None:

                if (
                    ordem_categorias[categoria_atual]
                    <
                    ordem_categorias[categoria_anterior]
                ):

                    regressoes_categoria_disposicao += 1


            categoria_anterior = categoria_atual


    diagnosticos.append(
        (
            "Regressões de categoria ao aumentar Necessidade: "
            f"{regressoes_categoria_necessidade}"
        )
    )

    diagnosticos.append(
        (
            "Regressões de categoria ao aumentar Disposição: "
            f"{regressoes_categoria_disposicao}"
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
    # 12. VALIDAÇÃO DA CONFIGURAÇÃO GENÉRICA DAS FASES
    # ========================================================

    verificar(
        fases.validar_configuracao(
            fase_1.CONFIGURACAO
        ),
        "Configuração Fase 1: contrato genérico válido"
    )


    # --------------------------------------------------------
    # SÍMBOLO EXTRA
    # --------------------------------------------------------

    config_extra = deepcopy(
        fase_1.CONFIGURACAO
    )


    config_extra[
        "transicoes"
    ]["q0"]["C"] = "q1"


    verificar(
        not automato.validar_determinismo(
            config_extra
        ),
        "Validação: rejeita símbolo fora do alfabeto"
    )


    # --------------------------------------------------------
    # MAIS DE UM ESTADO FINAL
    # --------------------------------------------------------

    config_multiplos_finais = deepcopy(
        fase_1.CONFIGURACAO
    )


    config_multiplos_finais[
        "estados_finais"
    ] = {
        "q2",
        "qf",
    }


    erro_multiplos_finais = False


    try:

        fases.validar_configuracao(
            config_multiplos_finais
        )


    except ValueError:

        erro_multiplos_finais = True


    verificar(
        erro_multiplos_finais,
        "Validação: rejeita múltiplos estados finais"
    )


    # --------------------------------------------------------
    # ARMADILHA SEM LIMITE DA MÉTRICA
    # --------------------------------------------------------

    config_armadilha_invalida = deepcopy(
        fase_1.CONFIGURACAO
    )


    config_armadilha_invalida[
        "estados_armadilha"
    ] = {
        "q1"
    }


    # O limite continua None propositalmente.

    erro_armadilha_sem_limite = False


    try:

        fases.validar_configuracao(
            config_armadilha_invalida
        )


    except ValueError:

        erro_armadilha_sem_limite = True


    verificar(
        erro_armadilha_sem_limite,
        "Validação: rejeita armadilha sem limite ativo"
    )
 

    # ========================================================
    # 13. REGISTRO DAS SETE FASES
    # ========================================================

    verificar(
        fases.fases_implementadas()
        == [1, 2, 3, 4, 5, 6, 7],
        "Registro: todas as sete fases implementadas"
    )


    # ========================================================
    # 14. VALIDAÇÃO DE TODAS AS FASES
    # ========================================================

    for numero_fase, configuracao in CONFIGURACOES_FASES.items():


        # ----------------------------------------------------
        # CONTRATO DA FASE
        # ----------------------------------------------------

        verificar(
            fases.validar_configuracao(
                configuracao
            ),
            f"Fase {numero_fase}: configuração válida"
        )


        # ----------------------------------------------------
        # ROTA DE REFERÊNCIA
        # ----------------------------------------------------

        rota = ROTAS_REFERENCIA[
            numero_fase
        ]


        estado, caminho, erro = automato.processar_sequencia(
            configuracao,
            configuracao["estado_inicial"],
            rota
        )


        verificar(
            (
                estado
                in configuracao["estados_finais"]
                and erro is None
            ),
            (
                f"Fase {numero_fase}: "
                f"rota {rota} chega ao final"
            ),
            (
                f"estado={estado}, "
                f"caminho={caminho}, "
                f"erro={erro}"
            )
        )


        # ----------------------------------------------------
        # TODOS OS ESTADOS SÃO ALCANÇÁVEIS
        # ----------------------------------------------------

        estados_configurados = set(
            configuracao[
                "nomes_estados"
            ].keys()
        )


        alcancaveis = estados_alcancaveis(
            configuracao
        )


        verificar(
            alcancaveis == estados_configurados,
            f"Fase {numero_fase}: todos os estados alcançáveis",
            (
                f"faltando="
                f"{estados_configurados - alcancaveis}"
            )
        )


        # ----------------------------------------------------
        # SOMENTE ARMADILHAS NÃO CHEGAM AO FINAL
        # ----------------------------------------------------

        sem_caminho_final = set()


        for estado in estados_configurados:

            if not consegue_alcancar_final(
                configuracao,
                estado
            ):

                sem_caminho_final.add(
                    estado
                )


        verificar(
            sem_caminho_final
            == set(
                configuracao[
                    "estados_armadilha"
                ]
            ),
            (
                f"Fase {numero_fase}: "
                "estados sem saída correspondem às armadilhas"
            ),
            (
                f"encontrado={sem_caminho_final}"
            )
        )


    # ========================================================
    # 15. ROTAS DE ARMADILHA
    # ========================================================

    for numero_fase, casos in ROTAS_ARMADILHA.items():

        configuracao = CONFIGURACOES_FASES[
            numero_fase
        ]


        for rota, armadilha_esperada in casos:

            estado, caminho, erro = automato.processar_sequencia(
                configuracao,
                configuracao["estado_inicial"],
                rota
            )


            verificar(
                (
                    estado == armadilha_esperada
                    and automato.eh_armadilha(
                        configuracao,
                        estado
                    )
                    and erro is None
                ),
                (
                    f"Fase {numero_fase}: "
                    f"rota {rota} chega em "
                    f"{armadilha_esperada}"
                ),
                (
                    f"estado={estado}, "
                    f"caminho={caminho}, "
                    f"erro={erro}"
                )
            )

    # ========================================================
    # BASE DE REGRAS FUZZY
    # ========================================================

    pares_regras = {
        (
            regra["necessidade"],
            regra["disposicao"]
        )
        for regra in fuzzy.REGRAS_FUZZY
    }


    combinacoes_esperadas = {

        ("baixa", "hostil"),
        ("baixa", "neutro"),
        ("baixa", "amigavel"),

        ("media", "hostil"),
        ("media", "neutro"),
        ("media", "amigavel"),

        ("alta", "hostil"),
        ("alta", "neutro"),
        ("alta", "amigavel"),
    }


    verificar(
        (
            len(fuzzy.REGRAS_FUZZY) == 9
            and pares_regras == combinacoes_esperadas
        ),
        "Fuzzy: base possui exatamente as nove combinações SE-ENTÃO"
    )


    saidas_validas_regras = all(

        regra["assistencia"] in {
            "nenhuma",
            "generica",
            "intermediaria",
            "especifica",
        }

        for regra in fuzzy.REGRAS_FUZZY
    )


    verificar(
        saidas_validas_regras,
        "Fuzzy: todas as regras possuem saída válida"
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


CONFIGURACOES_FASES = {

    1: fase_1.CONFIGURACAO,
    2: fase_2.CONFIGURACAO,
    3: fase_3.CONFIGURACAO,
    4: fase_4.CONFIGURACAO,
    5: fase_5.CONFIGURACAO,
    6: fase_6.CONFIGURACAO,
    7: fase_7.CONFIGURACAO,
}


ROTAS_REFERENCIA = {

    1: "AB",
    2: "BAB",
    3: "ABAB",
    4: "BBAB",
    5: "AABB",
    6: "ABBAB",
    7: "AABABB",
}


ROTAS_ARMADILHA = {

    4: [
        ("AAA", "qd"),
    ],

    5: [
        ("ABA", "qd"),
    ],

    6: [
        ("ABA", "qd1"),
        ("BAB", "qd2"),
    ],

    7: [
        ("AB", "qd1"),
        ("AABB", "qd2"),
    ],
}

def estados_alcancaveis(configuracao):
    """
    Retorna todos os estados alcançáveis a partir
    do estado inicial.
    """

    inicial = configuracao[
        "estado_inicial"
    ]

    visitados = {
        inicial
    }

    fila = [
        inicial
    ]


    while fila:

        estado = fila.pop(0)


        for destino in configuracao[
            "transicoes"
        ][estado].values():

            if destino not in visitados:

                visitados.add(
                    destino
                )

                fila.append(
                    destino
                )


    return visitados



def consegue_alcancar_final(
    configuracao,
    estado_inicial_teste
):
    """
    Verifica se existe algum caminho do estado informado
    até o estado final.
    """

    finais = set(
        configuracao["estados_finais"]
    )


    visitados = {
        estado_inicial_teste
    }


    fila = [
        estado_inicial_teste
    ]


    while fila:

        estado = fila.pop(0)


        if estado in finais:

            return True


        for destino in configuracao[
            "transicoes"
        ][estado].values():

            if destino not in visitados:

                visitados.add(
                    destino
                )

                fila.append(
                    destino
                )


    return False


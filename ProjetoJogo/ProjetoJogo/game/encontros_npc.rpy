# ============================================================
# CONTROLADOR GERAL DE ENCONTROS COM NPC
# ============================================================

# Este arquivo controla o início e o encerramento de encontros.
# Ele não contém conteúdo específico de nenhuma das fases
#
# As fases que decidem:
# - quando um encontro acontece;
# - onde acontece;
# - quais diálogos/interações estarão disponíveis.
#
# Este arquivo controlador aqui cuida de que
# - gerar a Disposição inicial;
# - classificar pela narração um vislumbre o NPC;
# - registrar o encontro;
# - permitir que o Navegador faça uma observação inicial do npc
#pra ajudar o jogador 


# ============================================================
# RESPOSTAS GERAIS - NPC NÃO FORNECE DICA
# ============================================================

# Estas respostas poderão ser utilizadas em qualquer fase
# quando a saída fuzzy indicar:
#
# NENHUMA ASSISTÊNCIA.

define RESPOSTAS_NPC_SEM_DICA = [

    "Não vou te dizer nada.",

    "Você vai ter que se virar.",

    "Humpf, Descubra o caminho sozinho então.",

]

# ============================================================
# INICIAR NOVO ENCONTRO
# ============================================================

label iniciar_encontro_npc:

    # Indica que existe um NPC ativo neste momento.
    $ npc_presente = True

    # Um novo encontro não herda a última saída fuzzy.
    $ resultado_fuzzy = None
    $ valor_assistencia_fuzzy = None
    $ categoria_assistencia = None

    # Conta quantos encontros aconteceram nesta fase.
    $ contador_encontros_npc += 1


    # ========================================================
    # DISPOSIÇÃO INICIAL
    # ========================================================

    # Cada novo NPC começa com uma Disposição diferente.
    #
    # Utilizamos o gerador aleatório do próprio Ren'Py
    # para manter compatibilidade com rollback e saves.

    $ disposicao_npc = renpy.random.randint(0, 100)


    # ========================================================
    # CLASSIFICAÇÃO NARRATIVA
    # ========================================================

    # Essa classificação serve SOMENTE para a percepção
    # apresentada pelo Navegador.
    #
    # Ela ainda não é a fuzzificação.

    $ classificacao_npc = npc.classificar_disposicao_narrativa(
        disposicao_npc
    )


    # ========================================================
    # REGISTRO DO ENCONTRO
    # ========================================================

    # Guardamos informações básicas para testes e,
    # futuramente, análise do comportamento do sistema.

    $ registro_encontro = {
        "encontro": contador_encontros_npc,
        "fase": fase_atual,
        "estado": estado_atual,
        "disposicao_inicial": disposicao_npc,
        "classificacao_inicial": classificacao_npc
    }


    $ historico_npc = historico_npc + [
        registro_encontro
    ]


    # ========================================================
    # PERCEPÇÃO DO NAVEGADOR
    # ========================================================

    call comentar_disposicao_npc


    return



# ============================================================
# NAVEGADOR COMENTA A DISPOSIÇÃO APARENTE
# ============================================================

label comentar_disposicao_npc:


    # --------------------------------------------------------
    # HOSTIL
    # --------------------------------------------------------

    if classificacao_npc == "hostil":

        navegador "Ele não parece muito amigável, capitão."

        navegador "Tome cuidado com o que vai dizer. Talvez ele não queira nos ajudar."


    # --------------------------------------------------------
    # NEUTRO
    # --------------------------------------------------------

    elif classificacao_npc == "neutro":

        navegador "Olha, capitão. Ele pode saber alguma coisa."

        navegador "Talvez valha a pena conversar com ele."


    # --------------------------------------------------------
    # AMIGÁVEL
    # --------------------------------------------------------

    elif classificacao_npc == "amigavel":

        navegador "Esse parece ser gente boa, capitão."

        navegador "Talvez esteja disposto a nos ajudar."


    return



# ============================================================
# ENCERRAR ENCONTRO
# ============================================================

label encerrar_encontro_npc:

    # O NPC deixa de estar ativo.

    $ npc_presente = False


    # Como cada encontro representa um novo Náufrago,
    # não carregamos a disposição para o próximo NPC.

    $ disposicao_npc = None

    $ classificacao_npc = None


    return

# ============================================================
# APLICAR ESCOLHA DO JOGADOR AO NPC
# ============================================================

label aplicar_escolha_npc(acao):

    # Guarda o valor anterior para registro.

    $ disposicao_anterior = disposicao_npc


    # Aplica o impacto cadastrado em npc.py.

    $ nova_disposicao, impacto_aplicado = npc.aplicar_interacao(
        disposicao_npc,
        acao
    )


    # Atualiza a disposição atual.

    $ disposicao_npc = nova_disposicao


    # Atualiza também a classificação narrativa interna.

    $ classificacao_npc = npc.classificar_disposicao_narrativa(
        disposicao_npc
    )


    # ========================================================
    # REGISTRO DA INTERAÇÃO
    # ========================================================

    $ registro_interacao = {

        "tipo": "interacao",

        "encontro": contador_encontros_npc,

        "fase": fase_atual,

        "estado": estado_atual,

        "acao": acao,

        "impacto": impacto_aplicado,

        "disposicao_anterior": disposicao_anterior,

        "disposicao_posterior": disposicao_npc,
    }


    $ historico_interacoes = historico_interacoes + [
        registro_interacao
    ]


    return

# ============================================================
# PRIMEIRA INTERAÇÃO COM O NÁUFRAGO
# ============================================================

label interacao_npc_inicial:

    naufrago "Estou aqui há horas."

    naufrago "Vocês têm água ou alguma coisa para comer?"


    menu:

        "Ajudar o Náufrago":

            call aplicar_escolha_npc(
                "ajudar"
            )

            naufrago "Obrigado. Isso vai me ajudar bastante."

            return "continuar"


        "Não ajudar":

            call aplicar_escolha_npc(
                "nao_ajudar"
            )

            naufrago "Entendi... achei que vocês poderiam ajudar."

            return "continuar"


        "Jogá-lo ao mar":

            call aplicar_escolha_npc(
                "jogar_ao_mar"
            )

            naufrago "Ei! O que você está fazendo?!"

            "Você empurra o Náufrago para o mar."

            return "encerrar"

# ============================================================
# SEGUNDA INTERAÇÃO COM O NÁUFRAGO
# ============================================================

label interacao_npc_social:

    naufrago "Vocês parecem conhecer estas águas melhor do que eu."


    menu:

        "Responder educadamente":

            call aplicar_escolha_npc(
                "conversar_educadamente"
            )

            naufrago "Pelo menos ainda existem pessoas educadas por aqui."


        "Insultá-lo":

            call aplicar_escolha_npc(
                "insultar"
            )

            naufrago "Não precisava falar assim."


        "Ignorá-lo":

            call aplicar_escolha_npc(
                "ignorar"
            )

            "Você ignora o comentário do Náufrago."


    return



# ============================================================
# NPC RECUSA FORNECER DICA
# ============================================================

label npc_recusar_dica:

    $ resposta_sem_dica = renpy.random.choice(
        RESPOSTAS_NPC_SEM_DICA
    )


    naufrago "[resposta_sem_dica]"


    return

# ============================================================
# CALCULAR ASSISTÊNCIA DO NPC
# ============================================================

label calcular_assistencia_npc:

    # Executa o sistema fuzzy utilizando:
    #
    # - Necessidade de Assistência atual do jogador;
    # - Disposição atual do NPC.

    $ resultado_fuzzy = fuzzy.calcular_assistencia(
        necessidade_assistencia,
        disposicao_npc
    )


    $ valor_assistencia_fuzzy = resultado_fuzzy[
        "valor"
    ]


    $ categoria_assistencia = resultado_fuzzy[
        "categoria"
    ]


    return

# ============================================================
# SOLICITAR AJUDA AO NPC
# ============================================================

label solicitar_ajuda_npc:

    # O jogador realizou uma nova solicitação de assistência.
    #
    # Essa solicitação entra na métrica Dicas Pedidas,
    # independentemente de o NPC efetivamente ajudar.

    $ dicas_pedidas += 1


    # A nova solicitação altera a Necessidade de Assistência.
    call atualizar_necessidade_assistencia


    # Com a Necessidade atualizada e a Disposição atual
    # do NPC, executamos o sistema fuzzy.
    call calcular_assistencia_npc


    # ========================================================
    # REGISTRO PARA TESTES FUTUROS
    # ========================================================

    $ registro_assistencia = {

        "tipo": "assistencia",

        "encontro": contador_encontros_npc,

        "fase": fase_atual,

        "estado": estado_atual,

        "necessidade_assistencia": necessidade_assistencia,

        "disposicao_npc": disposicao_npc,

        "valor_saida_fuzzy": valor_assistencia_fuzzy,

        "categoria": categoria_assistencia,
    }


    $ historico_interacoes = historico_interacoes + [
        registro_assistencia
    ]


    # ========================================================
    # EXECUTA A RESPOSTA CONCRETA
    # ========================================================

    if categoria_assistencia == "nenhuma":

        call npc_recusar_dica


    else:

        call fornecer_dica_npc_atual


    return


# ============================================================
# DECIDIR SE VAI PEDIR AJUDA AO NPC
# ============================================================

label decidir_ajuda_npc:

    naufrago "Bom... acho que vocês devem continuar a viagem."


    menu:

        "Perguntar sobre as ilhas":

            call solicitar_ajuda_npc


        "Ir embora":

            naufrago "Tudo bem. Boa sorte então."


    return



# ============================================================
# VERIFICAR ENCONTRO COM NPC
# ============================================================

label verificar_encontro_npc_atual:


    # ========================================================
    # CONFIGURAÇÃO DA FASE
    # ========================================================

    $ config_npc = configuracao_automato["npc"]

    $ modo_npc = config_npc["modo"]

    $ max_encontros = config_npc["max_encontros"]


    # ========================================================
    # FASE SEM NPC
    # ========================================================

    if modo_npc == "nenhum":

        return False


    # ========================================================
    # LIMITE DE ENCONTROS ATINGIDO
    # ========================================================

    if contador_encontros_npc >= max_encontros:

        return False


    # ========================================================
    # PROTEÇÃO
    # ========================================================

    # Mesmo que uma configuração incorreta consiga chegar
    # até aqui, NPCs somente aparecem em estados intermediários.

    if not automato.eh_intermediario(
        configuracao_automato,
        estado_atual
    ):

        return False


    # ========================================================
    # NPC FIXO
    # ========================================================

    if modo_npc == "fixo":

        $ estado_fixo = config_npc["estado_fixo"]


        if estado_atual == estado_fixo:

            call realizar_encontro_npc

            return True


        return False


    # ========================================================
    # NPC ALEATÓRIO
    # ========================================================

    if modo_npc == "aleatorio":

        $ chance_encontro = config_npc[
            "chance_encontro"
        ]


        # renpy.random é utilizado para manter compatibilidade
        # com o sistema de rollback/save do Ren'Py.

        $ sorteio_encontro = renpy.random.random()


        if sorteio_encontro < chance_encontro:

            call realizar_encontro_npc

            return True


    return False



# ============================================================
# REALIZAR ENCONTRO GENÉRICO
# ============================================================

label realizar_encontro_npc:


    "Há alguém nesta ilha."


    # ========================================================
    # CRIA O NOVO NPC
    # ========================================================

    call iniciar_encontro_npc


    naufrago "Ei! Vocês aí!"

    naufrago "Não esperava encontrar outro navio por aqui."


    # ========================================================
    # PRIMEIRA INTERAÇÃO
    # ========================================================

    call interacao_npc_inicial

    $ resultado_interacao = _return


    # ========================================================
    # JOGADO AO MAR
    # ========================================================

    if resultado_interacao == "encerrar":

        call encerrar_encontro_npc

        return


    # ========================================================
    # SEGUNDA INTERAÇÃO
    # ========================================================

    call interacao_npc_social


    # ========================================================
    # PEDIR OU NÃO AJUDA
    # ========================================================

    call decidir_ajuda_npc


    # ========================================================
    # ENCERRAR ENCONTRO
    # ========================================================

    call encerrar_encontro_npc


    return
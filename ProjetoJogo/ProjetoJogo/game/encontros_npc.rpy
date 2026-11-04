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
# INICIAR NOVO ENCONTRO
# ============================================================

label iniciar_encontro_npc:

    # Indica que existe um NPC ativo neste momento.
    $ npc_presente = True


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
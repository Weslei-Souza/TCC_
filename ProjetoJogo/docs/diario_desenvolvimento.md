# Diário de Desenvolvimento

## 25/10/2026

### Objetivo

Iniciar a implementação funcional do protótipo no Ren'Py e verificar a possibilidade de representar a navegação entre ilhas por meio de diferentes estados e transições.

### Implementado

- Criação e configuração inicial do projeto no Ren'Py.
- Criação dos personagens provisórios `Me` e `Navegador`.
- Criação da introdução do jogo com o navio no mar.
- Implementação da primeira estrutura de navegação entre ilhas utilizando `label`, `menu` e `jump`.
- Criação de três ilhas provisórias.
- Definição da Ilha 1 como estado inicial provisório da navegação.
- Implementação de caminhos de ida e retorno entre diferentes ilhas.
- Implementação proposital de ciclos entre as ilhas para testar o funcionamento contínuo das transições.

### Estrutura atual

O fluxo atual é:

```text
Introdução no mar
       |
       v
    Ilha 1
    /     \
   v       v
Ilha 2 → Ilha 3
   |         |
   └→ Ilha 1 ←┘
```

As transições atualmente implementadas são:

- Ilha 1 → Ilha 2
- Ilha 1 → Ilha 3
- Ilha 2 → Ilha 1
- Ilha 2 → Ilha 3
- Ilha 3 → Ilha 1

Nesta versão, o sistema permanece propositalmente em execução contínua, permitindo que o jogador navegue repetidamente entre os estados.


Ainda não foram implementados:

- estado final;
- estado armadilha/morto;
- registro do histórico de navegação;
- NPCs nas ilhas;
- sistema fuzzy;
- estado afetivo do NPC.

### Testes realizados

- [x] O jogo inicia corretamente.
- [x] A introdução leva à Ilha 1.
- [x] A Ilha 1 permite acessar as Ilhas 2 e 3.
- [x] A Ilha 2 permite retornar à Ilha 1.
- [x] A Ilha 2 permite acessar a Ilha 3.
- [x] A Ilha 3 permite retornar à Ilha 1.
- [x] As transições podem ser repetidas sem interromper a execução do jogo.

### Resultado da etapa

A navegação básica entre diferentes ilhas foi implementada com sucesso.

Essa estrutura servirá posteriormente como base para representar formalmente os estados e transições do autômato utilizado no jogo.

### Próximo passo

Adicionar à estrutura de navegação:

1. um estado final;
2. posteriormente, um estado armadilha;
3. organizar as ilhas como estados formais do primeiro autômato do jogo.

----------------------------------------------------------------

## 28/10/2026

### Planejamento da próxima etapa

Após a validação da navegação básica entre ilhas, foi definida como próxima etapa a criação de uma interface personalizada para seleção de rotas.

A interface deverá utilizar uma `screen` do Ren'Py, organizada inicialmente em duas colunas:

- personagem/NPC e informações da interação no lado esquerdo;
- opções de rotas/botões no lado direito.

Também foi definido que a navegação começará a representar explicitamente os estados de um autômato.

Mapeamento inicial provisório:

- Ilha 1 → `q0` — estado inicial;
- Ilha 2 → `q1`;
- Ilha 3 → `q2`.

Posteriormente serão adicionados um estado final e um estado armadilha.

Foi discutida também uma funcionalidade futura em que o jogador poderá informar uma sequência de símbolos, como `AAB` ou `010`, para representar uma palavra de entrada. O sistema deverá processar essa sequência a partir do estado inicial e percorrer automaticamente as ilhas correspondentes às transições realizadas.

Essa funcionalidade será implementada somente após a formalização dos estados e da tabela de transições.

### Ordem definida

1. Criar interface personalizada para escolha de rotas.
2. Associar as ilhas a estados formais.
3. Implementar estado final e estado armadilha.
4. Definir transições do primeiro autômato.
5. Implementar entrada e processamento de sequências.

## Organização inicial da arquitetura

O código do protótipo passou a ser organizado em arquivos com responsabilidades distintas.

### script.rpy

Responsável pelo ponto de entrada do jogo, definição dos personagens e inicialização de variáveis globais.

### screens.rpy

Responsável pela interface gráfica.

Foi definida uma tela reutilizável de escolha de rotas, organizada em duas colunas:

- lado esquerdo: personagem/NPC e informações da interação;
- lado direito: botões correspondentes às rotas disponíveis.

A tela retorna apenas o símbolo da transição escolhida (`A` ou `B`), sem determinar diretamente o próximo estado.

### ilhas.rpy

Responsável pelos estados e fluxo atual do jogo.

Cada ilha possui um `label` associado provisoriamente a um estado do autômato:

- Ilha 1 → q0;
- Ilha 2 → q1;
- Ilha 3 → q2;
- Ilha Final → qf.

Os labels recebem a escolha retornada pela interface e atualmente determinam o próximo estado.

Essa implementação ainda será posteriormente substituída por uma lógica formal de transições.

### Decisão de arquitetura

A interface deverá permanecer separada da lógica formal do autômato.

Posteriormente, o processamento das transições será transferido para código Python independente, permitindo que o Ren'Py seja responsável principalmente pela apresentação e interação com o jogador.
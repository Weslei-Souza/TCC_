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
# Diário de Desenvolvimento — 27/10 e 28/10/2026

## Situação do projeto

O desenvolvimento do protótipo em Ren'Py avançou da navegação básica entre telas para uma estrutura mais próxima do jogo proposto no TCC.

A navegação entre ilhas já estava funcional, com a Ilha 1 funcionando como estado inicial provisório e com possibilidade de alcançar um estado final, encerrando corretamente a partida.

## Implementações e decisões consolidadas

### 1. Estrutura do autômato

Foi mantida a correspondência entre as ilhas e os estados do autômato:

- Ilha 1 → `q0` — estado inicial;
- Ilha 2 → `q1`;
- Ilha 3 → `q2`;
- Ilha Final → `qf` — estado final.

As rotas `A` e `B` representam as transições entre esses estados.

O autômato utilizado atualmente ainda é provisório e serve principalmente para desenvolver e testar a infraestrutura do jogo.

### 2. Organização modular do projeto

Foi definida uma separação de responsabilidades entre os arquivos do projeto.

`script.rpy`
- ponto de entrada do jogo;
- personagens;
- variáveis globais;
- estado atual da partida;
- modo selecionado;
- fase atual.

`screens.rpy`
- interfaces;
- botões;
- seleção de modo;
- seleção de fases;
- tutorial;
- mapa;
- tela de escolha de transições.

`ilhas.rpy`
- representação visual das ilhas/estados.

`navegacao.rpy`
- fluxo dos modos de jogo;
- navegação passo a passo;
- processamento de rota completa;
- vitória.

`logica/automato.py`
- representação formal dos estados;
- tabela de transições;
- função de transição;
- processamento de sequências.

`logica/fases.py`
- configuração das fases e progressão.

Também foi organizada a estrutura de imagens em pastas separadas para fundos, personagens e interface.

### 3. Integração Ren'Py e Python

Foi planejada/adotada a separação entre a interface Ren'Py e a lógica computacional em Python.

A ideia central é:

Ren'Py  
→ recebe a ação do jogador  
→ envia estado e símbolo ao Python  
→ Python calcula a transição  
→ devolve o novo estado  
→ Ren'Py apresenta a nova ilha.

O módulo Python deve permanecer independente da interface e não deverá armazenar diretamente o estado corrente da partida.

### 4. Dois modos de jogo

Foram definidos dois modos que utilizam o mesmo autômato.

#### Navegação passo a passo

O jogador escolhe cada transição individualmente.

Exemplo:

`q0 → A → q1 → B → q2`

#### Planejamento de rota

O jogador informa uma sequência completa, como:

`ABB`

O sistema processa todos os símbolos sequencialmente e determina o estado final alcançado.

Exemplo:

`q0 → q1 → q2 → qf`

Depois de terminar em um estado não final, o jogador poderá informar uma nova sequência a partir daquele ponto.

### 5. Menu e fluxo geral

Foi definido que o fluxo deverá ser:

Menu principal  
→ seleção do modo de jogo  
→ seleção da fase  
→ início da partida.

O menu deverá também oferecer acesso a uma explicação de como o jogo funciona.

### 6. Mapa

Foi planejada a transformação do mapa textual em um mapa visual do arquipélago.

O mapa deverá mostrar:

- miniaturas das ilhas;
- identificação dos estados (`q0`, `q1`, `q2`, `qf`);
- indicação do estado inicial;
- indicação do estado final;
- rotas;
- símbolos das transições.

As próprias imagens das ilhas poderão ser reaproveitadas como miniaturas.

### 7. Tutorial

Foi decidido que a tela "Como jogar" deverá utilizar uma área rolável.

O tutorial poderá apresentar gradualmente:

- objetivo do jogo;
- estado inicial;
- estados intermediários;
- estado final;
- transições;
- símbolos `A` e `B`;
- funcionamento do modo Navegação;
- funcionamento do modo Planejamento.

O jogo continua sendo tratado como material didático/de apoio e não como ferramenta cuja eficácia de aprendizagem já foi comprovada.

### 8. Progressão de fases

Foi definida provisoriamente uma estrutura com sete fases.

Apenas a primeira precisa estar implementada neste momento.

Estrutura conceitual futura:

1. conceitos básicos: estado inicial, estados intermediários e estado final;
2. novas rotas;
3. caminhos alternativos;
4. introdução de loop, possivelmente representado por um redemoinho;
5. rotas mais complexas;
6. estado morto/armadilha, possivelmente representado por uma prisão;
7. desafio final combinando conceitos anteriores.

As fases deverão ser desbloqueadas progressivamente.

Uma fase ainda não implementada poderá aparecer como "Em desenvolvimento".

### 9. Variáveis preparadas para o jogador

Foram definidas como variáveis candidatas:

- número de tentativas;
- quantidade de retornos;
- estados repetidos;
- entradas em estados armadilha;
- solicitações anteriores de ajuda;
- histórico de estados;
- histórico de interações.

Essas variáveis ainda não devem ser interpretadas como emoções.

Posteriormente poderão contribuir para uma medida operacional de **necessidade de assistência**.

### 10. Estado do NPC

Foi mantida a decisão de preparar:

- uma variável de estado afetivo interno do NPC;
- um histórico de interações.

Nenhuma escala, peso ou significado matemático definitivo foi definido ainda.

As escolhas futuras do jogador deverão atualizar o estado interno do NPC, que posteriormente será fuzzificado.

### 11. Interface visual

Foram planejadas melhorias para deixar o protótipo com aparência mais próxima de um jogo:

- remover caixas excessivas;
- utilizar painéis sólidos ou imagens de interface;
- posicionar o Navegador próximo das opções de rota;
- utilizar o fundo marítimo também nos menus;
- adaptar as imagens à resolução do projeto;
- utilizar os nomes dos arquivos como tags automáticas do Ren'Py sempre que possível.

## Próximas implementações

A ordem de trabalho definida para a sequência do desenvolvimento é:

1. finalizar o fluxo visual dos menus;
2. fazer o Navegador aparecer corretamente nas telas de escolha;
3. ajustar fundos, painéis e imagens;
4. terminar o mapa visual;
5. terminar o tutorial rolável;
6. finalizar seleção e desbloqueio das sete fases;
7. começar a registrar automaticamente o histórico de estados;
8. contabilizar tentativas;
9. detectar estados repetidos;
10. definir e implementar o conceito de retorno;
11. adicionar pedidos de ajuda;
12. fazer o modo de rota completa mostrar visualmente o percurso pelas ilhas;
13. implementar o estado interno do NPC;
14. definir a necessidade de assistência;
15. somente depois implementar o sistema fuzzy.

## Estado ao final do dia

O projeto deixou de ser apenas um teste de transição entre labels e passou a possuir uma arquitetura definida para:

- interface;
- autômato;
- dois modos de navegação;
- processamento Python;
- mapa;
- tutorial;
- fases;
- progressão;
- futuras métricas do jogador;
- futuro estado afetivo do NPC;
- futura integração fuzzy.

O foco seguinte será concluir a infraestrutura visual e de progressão antes de iniciar a coleta efetiva das métricas utilizadas pelo mecanismo adaptativo.

# ===============================================
# Diário de Desenvolvimento — 29/10/2026

## Situação geral

O projeto avançou da navegação básica para uma arquitetura modular capaz de suportar múltiplas fases, processamento de autômatos em Python e coleta de métricas reais do jogador.

A versão atual foi testada e está funcionando sem erros após a refatoração.

## Atividades realizadas

### 1. Testes das métricas de navegação

Foram realizados testes com percursos simples e longos nos dois modos de jogo.

Foram validados:

- histórico dos estados visitados;
- contagem de estados repetidos;
- identificação de retornos.

Os testes indicaram que essas métricas estão sendo processadas corretamente.

### 2. Integração com `jogador.py`

O módulo `jogador.py` passou a analisar o percurso realizado pelo jogador.

O Ren'Py continua responsável por armazenar o estado da partida, enquanto o Python recebe os dados, processa as métricas e devolve os resultados.

### 3. Refatoração do autômato

Foi realizada a separação entre:

**motor genérico do autômato**
- processamento de transições;
- identificação de estado inicial;
- identificação de estados finais;
- processamento de sequências;

e:

**configuração específica da Fase 1**
- estados;
- nomes das ilhas;
- transições;
- estado inicial;
- estado final.

Foi criada uma estrutura específica para os autômatos das fases, permitindo futuramente adicionar novas fases sem alterar o motor geral.

### 4. Estrutura preparada para múltiplas fases

`automato.py` passou a funcionar como motor genérico.

A configuração da Fase 1 foi movida para um módulo próprio.

`fases.py` passou a relacionar cada fase à configuração de seu respectivo autômato.

Essa mudança permite futuramente ter:

- `fase_1.py`;
- `fase_2.py`;
- `fase_3.py`;
- etc.

sem duplicar a lógica geral.

### 5. Correções durante a refatoração

Foram corrigidos problemas de integração relacionados a:

- configuração da Fase 1;
- chamadas do motor genérico;
- passagem da configuração do autômato para as funções;
- chamadas de `nome_estado`;
- chamadas de `transicao`;
- processamento de sequências.

Após as correções, o jogo voltou a funcionar normalmente.

### 6. Versionamento

As alterações foram commitadas no GitHub.

O GitHub Desktop passou a ser utilizado como ferramenta principal de versionamento por ser mais prático para o fluxo atual.

Continuar utilizando nomes claros de commit para registrar cada marco de desenvolvimento.

---

# Próximas tarefas definidas

## Prioridade 1 — Isolar completamente as fases no Ren'Py

Criar uma estrutura específica para o conteúdo Ren'Py das fases, semelhante à separação já realizada no Python.

Objetivo futuro:

```text
game/
└── fases/
    ├── fase_1.rpy
    ├── fase_2.rpy
    ├── fase_3.rpy
    └── ...
```

A Fase 1 deverá concentrar:

- imagens específicas;
- estados visuais;
- textos;
- labels;
- elementos narrativos;
- demais conteúdos exclusivos da fase.

Também será criado um despachante genérico que utiliza `fase_atual` para determinar qual conteúdo deve ser apresentado.

Será definido um padrão de nomenclatura única para os assets, por exemplo:

- `bg_ilha1_fase1`;
- `bg_ilha2_fase1`;
- `bg_ilha3_fase1`;
- `bg_final_fase1`.

Essa tarefa deverá fechar completamente a Fase 1 como unidade isolada.

## Tarefa sequencial 1 — Ajuda e reinício

Após concluir a reorganização das fases, implementar:

- botão `Pedir ajuda`;
- botão `Reiniciar fase`.

Será preparada uma estrutura contendo:

- dicas genéricas;
- dicas específicas de cada fase.

Neste momento as dicas ainda não utilizarão lógica fuzzy.

## Tarefa sequencial 2 — Definir tentativa

Depois disso será formalizado o conceito de `tentativa`.

Weslei apresentará uma proposta de funcionamento.

Antes da implementação, a lógica será revisada para identificar:

- ambiguidades;
- situações inconsistentes;
- métricas que possam ser contabilizadas incorretamente;
- diferenças entre os modos de navegação e planejamento.

Somente após essa revisão a variável `numero_tentativas` será incorporada definitivamente.

## Tarefa sequencial 3 — NPC

Depois será iniciada a implementação das interações com o NPC.

Nome provisório:

- Pirata Perdido; ou
- Náufrago.

Serão criadas:

- interações;
- escolhas de diálogo/ações;
- histórico das interações;
- estrutura necessária para alteração futura do estado interno afetivo.

## Tarefa sequencial 4 — Necessidade de assistência

Posteriormente será definida formalmente a variável de necessidade de assistência.

Será necessário decidir:

- nome definitivo;
- quais métricas participarão;
- forma de cálculo;
- escala utilizada;
- significado da saída;
- forma como essa saída será posteriormente fuzzificada.

Somente depois serão definidos pesos, funções de pertinência ou regras fuzzy.

## Etapas posteriores

Após essas tarefas:

- definir estado afetivo do NPC;
- definir seus eventos e impactos;
- implementar o sistema fuzzy;
- integrar necessidade de assistência + estado afetivo;
- utilizar a saída fuzzy para selecionar nível de ajuda;
- expandir novas fases;
- implementar loop/redemoinho;
- implementar estado morto/armadilha/prisão;
- desenvolver testes sistemáticos e resultados.}

# Diário de Desenvolvimento — 30/10/2026

## Situação geral

O desenvolvimento avançou em duas frentes principais:

1. **reestruturação arquitetural do projeto para suporte a múltiplas fases**;
2. **implementação inicial dos mecanismos de assistência ao jogador**.

Ao final do dia, a Fase 1 continuou funcionando corretamente após as refatorações, e foram adicionados os controles de mapa, dicas e reinício de fase.

Também foi feita uma pausa na implementação para discutir conceitos que deverão ser definidos antes da construção do modelo afetivo e fuzzy.

---

## 1. Isolamento do conteúdo Ren'Py das fases

A estrutura do projeto foi reorganizada para separar o conteúdo específico das fases do código geral do jogo.

Foi criada uma estrutura semelhante a:

```text
game/
│
├── script.rpy
├── screens.rpy
├── navegacao.rpy
│
├── fases/
│   ├── despachante_fases.rpy
│   └── fase_1.rpy
│
└── logica/
    ├── automato.py
    ├── fases.py
    ├── jogador.py
    ├── npc.py
    ├── fuzzy.py
    └── automatos/
        └── fase_1.py
```

A divisão ficou conceitualmente organizada da seguinte forma:

### `logica/automatos/fase_1.py`

Contém a definição formal do autômato da Fase 1:

- estados;
- estado inicial;
- estado final;
- transições;
- nomes dos estados.

### `fases/fase_1.rpy`

Contém a representação da Fase 1 no jogo:

- imagens;
- textos;
- representação visual dos estados;
- mapa específico;
- posteriormente, dicas e demais elementos exclusivos da fase.

### `fases/despachante_fases.rpy`

Passou a funcionar como camada intermediária entre o sistema geral e o conteúdo específico das fases.

Exemplo conceitual:

```text
navegacao.rpy
      ↓
exibir_ilha_atual
      ↓
despachante
      ↓
fase_atual
      ↓
fase_1_exibir_estado
```

Isso permite futuramente criar:

```text
fase_2.rpy
fase_3.rpy
...
```

sem alterar o sistema geral de navegação.

---

## 2. Padronização dos assets das fases

Foi definida a necessidade de utilizar nomes exclusivos para os assets de cada fase.

Exemplo de padrão:

```text
bg_ilha1_fase1
bg_ilha2_fase1
bg_ilha3_fase1
bg_final_fase1
```

O objetivo é evitar conflitos quando novas fases utilizarem imagens de ilhas próprias.

O `bg_mar` e elementos gerais do jogo permanecem fora dessa nomenclatura específica.

---

## 3. Separação do mapa da Fase 1

O mapa também foi identificado como conteúdo específico da fase.

Assim, sua responsabilidade foi deslocada para a estrutura da Fase 1.

Foi criado um despachante para que a interface geral possa chamar apenas:

```text
mapa_atual
```

e o sistema determine qual mapa apresentar de acordo com `fase_atual`.

Conceitualmente:

```text
botão Mapa
    ↓
mapa_atual
    ↓
fase_atual
    ↓
mapa_fase_1
```

---

## 4. Controles gerais da partida

Foi definida a interface básica da fase com três controles principais:

```text
Mapa
Dica
Reiniciar
```

A decisão atual é não adicionar outros botões obrigatórios neste momento.

Um eventual botão para sair da fase ou retornar ao menu poderá ser avaliado posteriormente.

A disposição visual planejada é:

```text
[ MAPA ]                         [ DICA ] [ REINICIAR ]
```

O mapa permanece separado, enquanto Dica e Reiniciar ficam agrupados.

O acabamento visual ainda não é prioridade.

---

## 5. Sistema de reinício da fase

Foi implementado o botão:

```text
Reiniciar
```

Seu comportamento atual é:

- retornar o jogador ao estado inicial do autômato;
- reiniciar o histórico do percurso atual;
- manter as métricas acumuladas da partida.

Foi adicionada a variável:

```text
numero_resets
```

Ela registra quantas vezes o jogador reiniciou a fase.

Essa métrica poderá futuramente participar do cálculo da necessidade de assistência.

### Decisão atual

Ao reiniciar:

```text
estado_atual
historico_estados
```

são reiniciados.

Entretanto, permanecem acumulados:

```text
numero_resets
estados_repetidos
quantidade_retornos
pedidos_ajuda
```

A intenção é preservar informações sobre o comportamento anterior do jogador.

---

## 6. Sistema inicial de dicas

Foi implementado um sistema de dicas ainda independente de lógica fuzzy.

Existem dois grupos de dicas:

### Dicas gerais

Podem ser utilizadas independentemente da fase.

Exemplos:

- observar o mapa;
- lembrar que letras representam transições;
- verificar o estado atual antes de escolher uma rota.

### Dicas específicas

Permanecem dentro do arquivo de cada fase.

Para a Fase 1, foram definidas atualmente:

> “Nesta fase, a Ilha 1 representa o estado inicial q0, e a Ilha Final representa o estado final qf.”

> “A Ilha 3 está próxima do objetivo final desta fase.”

> “Você não precisa passar pela Ilha 2 para chegar à Ilha Final, mas pode ser necessário dependendo da rota escolhida.”

---

## 7. Funcionamento das dicas

Ao iniciar a fase, o sistema monta uma lista contendo:

```text
dicas gerais
+
dicas específicas da fase
```

Quando o jogador solicita ajuda:

1. uma dica é selecionada aleatoriamente;
2. a dica é exibida;
3. ela é removida da lista disponível;
4. não pode ser sorteada novamente naquela partida.

Quando todas as dicas já foram apresentadas, o NPC informa:

```text
“Sem mais dicas pra você!”
```

Também foi mantida a variável:

```text
pedidos_ajuda
```

para registrar o uso do sistema de assistência.

A definição exata dessa métrica ainda deverá ser revisada: poderá representar apenas dicas efetivamente fornecidas ou todas as solicitações feitas pelo jogador.

---

## 8. Testes realizados

Foram realizados testes dos novos controles nos dois modos de jogo.

### Sistema de dicas

Foi verificado:

- sorteio das dicas;
- remoção após utilização;
- ausência de repetição;
- esgotamento correto da lista;
- mensagem de ausência de novas dicas.

### Reinício

Foi verificado:

- retorno ao estado inicial;
- atualização de `numero_resets`;
- reinício do histórico do percurso atual;
- preservação das métricas acumuladas.

### Navegação

Também foi confirmado que os mecanismos anteriores continuam funcionando:

- histórico de estados;
- estados repetidos;
- retornos;
- navegação passo a passo;
- planejamento de sequência;
- chegada ao estado final.

Os códigos temporários de debug foram removidos após a validação.

---

# 9. Pausa na implementação para decisões conceituais

Após estabilizar essa etapa, decidiu-se interromper temporariamente a implementação para discutir conceitos antes da reunião com a orientadora.

O principal objetivo é evitar definir pesos, escalas ou regras fuzzy arbitrariamente.

---

## 10. Necessidade de Assistência

Foi retomada a ideia de construir uma variável intermediária provisoriamente chamada:

```text
Necessidade de Assistência
```

Ela deverá ser obtida a partir de métricas observáveis do comportamento do jogador.

Métricas candidatas atualmente:

```text
tentativas
estados repetidos
retornos
reinícios
solicitações de ajuda
entrada em estados mortos/armadilhas
```

A arquitetura preferida até o momento é:

```text
métricas do jogador
        ↓
normalização/combinação
        ↓
Índice de Necessidade de Assistência
        ↓
fuzzificação
        ↓
Baixa / Média / Alta
```

Ainda não foi definido:

- se haverá média;
- se será média ponderada;
- quais métricas terão maior peso;
- como os pesos serão justificados;
- qual escala será utilizada.

---

## 11. Possível redundância entre métricas

Foi identificada uma questão metodológica importante.

Um único comportamento pode aumentar simultaneamente:

```text
estados repetidos
retornos
tentativas
```

Isso pode fazer com que o mesmo comportamento seja contabilizado várias vezes no cálculo da necessidade de assistência.

Será necessário discutir:

- quais métricas representam fenômenos realmente distintos;
- quais são parcialmente redundantes;
- quais devem ser combinadas ou descartadas.

---

## 12. Definição de tentativa ainda pendente

A variável:

```text
numero_tentativas
```

ainda não possui uma definição operacional definitiva.

Foi levantada como possibilidade:

> Uma tentativa começa no estado inicial e termina quando o jogador alcança o estado final, reinicia o percurso ou entra em uma condição que impossibilite a continuação.

Entretanto, a definição deverá ser revisada separadamente para:

- modo passo a passo;
- modo planejamento de rota.

Weslei apresentará sua proposta antes da implementação definitiva.

---

## 13. Estado interno do NPC

Foi reforçada a arquitetura anteriormente definida:

```text
interações do jogador
        ↓
impactos positivos/negativos
        ↓
valor interno contínuo do NPC
        ↓
fuzzificação
        ↓
estado linguístico
```

Ainda não foram definidos:

- escala;
- pesos dos eventos;
- limites;
- função de atualização;
- funções de pertinência.

Também foi discutido que o nome da variável precisa ser escolhido com cuidado.

Opções consideradas:

```text
Estado afetivo interno do NPC
Valência afetiva do NPC
Disposição afetiva do NPC
```

A expressão `estado afetivo interno` permanece a alternativa mais geral por enquanto.

Caso a variável represente especificamente um eixo negativo–positivo, `valência afetiva` poderá ser conceitualmente mais precisa.

---

## 14. Estado afetivo versus disposição para ajudar

Foi identificada uma distinção importante.

Não é desejável utilizar diretamente:

```text
disposição para ajudar
```

como entrada do modelo, porque isso se aproxima demais da própria saída esperada.

A arquitetura preferida permanece:

```text
estado afetivo do NPC
+
necessidade de assistência do jogador
        ↓
sistema fuzzy
        ↓
nível de assistência
```

Assim, o estado afetivo influencia a disposição para ajudar, mas não é sinônimo dela.

---

## 15. Arquitetura conceitual atual

O modelo discutido atualmente pode ser representado da seguinte forma:

```text
                    JOGADOR
                       │
          ┌────────────┴────────────┐
          │                         │
       navegação                interações
          │                         │
          ▼                         ▼
   repetições                 escolhas
   retornos                   eventos
   resets                     diálogos
   tentativas                     │
   pedidos de ajuda                ▼
          │                 Estado afetivo
          ▼                    do NPC
  Necessidade de                   │
    Assistência                    │
          │                        │
          └───────────┬────────────┘
                      ▼
                SISTEMA FUZZY
                      │
                      ▼
             Nível de assistência
                      │
                      ▼
                resposta/dica
```

---

# 16. Questões preparadas para a reunião com a orientadora

Foram levantadas questões para discussão:

- A Necessidade de Assistência deve ser uma única variável calculada antes do fuzzy?
- Deve ser utilizada média simples, média ponderada ou outra abordagem?
- Como justificar pesos diferentes para cada métrica?
- As métricas precisam ser normalizadas antes da combinação?
- Repetições, retornos e reinícios são suficientemente independentes?
- Qual deve ser a definição formal de tentativa?
- `pedidos_ajuda` deve representar dicas fornecidas ou solicitações realizadas?
- Qual o melhor nome para o estado interno do NPC?
- Qual escala utilizar para essa variável?
- Os impactos das interações serão fixos ou acumulativos?
- Deve existir decaimento do estado afetivo?
- Faz sentido utilizar três conjuntos fuzzy por

# Diário de Desenvolvimento — Atualização de 31/10 a 04/11/2026

## 31/10/2026 — Consolidação da estrutura e preparação das próximas implementações

O desenvolvimento permaneceu concentrado na consolidação da estrutura já construída para o protótipo. Os testes realizados anteriormente sobre histórico de estados, estados repetidos e navegação nos dois modos continuaram apresentando resultados coerentes. O fluxo entre Ren'Py e os módulos Python permaneceu funcional tanto no modo de navegação passo a passo quanto no modo de planejamento de rota.

A organização modular do projeto foi mantida, separando a lógica geral do autômato, o conteúdo específico das fases e os elementos de interface. O objetivo dessa separação passou a ser permitir que, futuramente, novas fases pudessem utilizar o mesmo motor lógico e alterar apenas sua configuração específica.

Também foi mantido o uso do GitHub Desktop para controle de versão, com commits progressivos das funcionalidades implementadas.

Neste momento, o próximo foco passou a ser a definição das variáveis utilizadas para representar o comportamento do jogador e o estado interno dos NPCs, visando preparar a integração posterior com o sistema fuzzy.

---

## 01/11/2026 — Manutenção das decisões arquiteturais

Não houve alteração estrutural significativa no protótipo neste período. Foram mantidas como prioridades a estabilização do sistema atual, a definição das métricas do jogador e a preparação da futura integração entre Necessidade de Assistência, estado interno do NPC e lógica fuzzy.

Permaneceu a decisão de evitar expansão desnecessária do escopo visual ou de mecânicas antes da conclusão do núcleo computacional.

---

## 02/11/2026 — Reunião de orientação e redefinição do MVP

A reunião com a orientadora foi utilizada para revisar o escopo do projeto e reduzir funcionalidades que poderiam aumentar excessivamente o tempo de desenvolvimento.

Foi reafirmado que o trabalho deve priorizar um protótipo funcional, com foco na contribuição computacional central, e não em um jogo completo ou visualmente sofisticado.

O núcleo mínimo definido para o protótipo passou a incluir:

- representação de autômatos e navegação entre estados;
- interação com NPCs;
- estado interno do NPC;
- cálculo de Necessidade de Assistência;
- sistema fuzzy;
- assistência adaptativa;
- progressão simples entre fases;
- menus e controles básicos.

Também foi reforçada a decisão de utilizar somente autômatos determinísticos no TCC. A implementação de autômatos não determinísticos foi reservada para trabalhos futuros.

A interface lúdica também foi separada da representação formal. Os identificadores internos do autômato, como `q0`, `q1` e `qf`, continuam sendo utilizados na implementação, mas deixaram de ser apresentados diretamente ao jogador. Na interface são utilizados nomes como Ilha 1, Ilha 2 e Ilha Final.

Foi consolidada a definição operacional de tentativa:

“Uma tentativa é um ciclo de execução da fase iniciado no estado inicial e encerrado por conclusão, reinício ou abandono da fase.”

Apesar dessa definição permanecer documentada, decidiu-se posteriormente que o número de tentativas não entraria no cálculo da Necessidade de Assistência, evitando duplicidade com a métrica de reinícios.

Também foi consolidada a justificativa metodológica inicial para os pesos das métricas:

“Os pesos foram definidos a priori com base na interpretação funcional de cada métrica no contexto da tarefa, atribuindo maior influência a comportamentos que representam interrupção ou incapacidade de prosseguir autonomamente.”

---

## 03/11/2026 — Implementação da Necessidade de Assistência

Foi implementado o cálculo da Necessidade de Assistência do jogador no módulo `logica/jogador.py`.

As métricas utilizadas foram definidas como:

- Reinícios: peso 0,35;
- Dicas pedidas: peso 0,25;
- Estados repetidos: peso 0,15;
- Armadilhas: peso 0,25.

O número de tentativas foi retirado do cálculo. A decisão foi tomada porque cada reinício já representa o encerramento de uma tentativa e o início de outra. Utilizar simultaneamente reinícios e número de tentativas poderia representar uma dupla valorização do mesmo comportamento.

Cada métrica passou a ser normalizada para o intervalo entre 0 e 1 por meio de um limite de referência específico da fase.

A normalização utilizada foi:

`n_i = min(valor_observado / limite_de_referencia, 1)`

A Necessidade de Assistência passou a ser calculada por média ponderada:

`NA = 100 × [Σ(w_i × n_i) / Σ(w_i ativos)]`

Métricas inexistentes em determinada fase não participam do cálculo. Dessa forma, seus pesos também são retirados do denominador.

Na configuração provisória da Fase 1 foram definidos os seguintes limites:

Reinícios = 3  
Dicas pedidas = 3  
Estados repetidos = 3  
Armadilhas = não aplicável

Os limites foram tratados como parâmetros iniciais de projeto e não como valores empiricamente validados. A intenção é posteriormente verificar sua adequação por meio de cenários simulados.

Foram realizados testes manuais do cálculo. Entre os resultados confirmados:

- uma dica solicitada produziu aproximadamente 11,11;
- três dicas produziram aproximadamente 33,33;
- três reinícios produziram aproximadamente 46,67;
- uma ocorrência de cada métrica ativa produziu aproximadamente 33,33;
- saturação de todas as métricas ativas produziu 100.

Os resultados obtidos coincidiram com os valores calculados manualmente.

Durante essa etapa também foram eliminados resíduos de versões anteriores, como a métrica de retornos, referências antigas a `pedidos_ajuda` e chamadas que ainda esperavam três valores de retorno da função `registrar_percurso`.

---

## 04/11/2026 — Implementação do NPC e da Disposição Afetiva

Foi iniciada e concluída a primeira implementação funcional do sistema de NPC.

O módulo `logica/npc.py` passou a controlar uma variável contínua denominada, no código, Disposição do NPC e, na escrita acadêmica, Disposição Afetiva.

A variável utiliza o intervalo de 0 a 100.

Cada novo encontro recebe um valor inicial aleatório dentro dessa escala. A decisão de não utilizar sempre o valor 50 teve como objetivo permitir que encontros distintos comecem em condições diferentes e produzam comportamentos variados.

A geração do valor inicial é realizada pelo Ren'Py, enquanto `npc.py` permanece responsável pelas operações matemáticas sobre a variável.

Foi criada uma classificação narrativa simples para permitir ao Navegador fornecer ao jogador uma percepção aproximada do NPC antes da interação:

0 a 33 → hostil  
34 a 66 → neutro  
67 a 100 → amigável

Essa classificação é utilizada apenas para a narrativa e não representa a fuzzificação propriamente dita.

O encontro tutorial da Fase 1 foi configurado para ocorrer de maneira fixa na Ilha 3. Essa decisão foi utilizada apenas na versão atual da fase, garantindo que o jogador encontre o NPC antes de chegar à Ilha Final.

Foi criado o arquivo `encontros_npc.rpy`, responsável pelo controle geral dos encontros.

O sistema passou a registrar informações como:

- número do encontro;
- fase;
- estado em que ocorreu;
- disposição inicial;
- classificação narrativa;
- ações realizadas;
- impacto das ações;
- disposição anterior;
- disposição posterior.

### Interações e impactos na Disposição

Foram implementadas duas etapas de interação antes da possibilidade de solicitar ajuda.

Na primeira etapa:

Ajudar o Náufrago → +20  
Não ajudar → -10  
Jogar o Náufrago ao mar → -40 e encerramento imediato do encontro

Na segunda etapa:

Responder/conversar educadamente → +10  
Insultar → -20  
Ignorar → -5

Os impactos foram definidos como valores fixos para manter interpretabilidade, reprodutibilidade e facilidade de validação.

A variável é limitada ao intervalo 0–100. Portanto, valores resultantes inferiores a zero são convertidos para zero e valores superiores a 100 são limitados a 100.

Somente após essas interações o jogador recebe a opção de:

“Perguntar sobre as ilhas”

ou

“Ir embora”.

A escolha “Ir embora” encerra a conversa sem alterar a métrica de dicas.

Ao selecionar “Perguntar sobre as ilhas”, ocorre o seguinte fluxo:

`dicas_pedidas += 1`

→ recálculo da Necessidade de Assistência

→ execução do sistema fuzzy

→ escolha do nível de assistência

→ resposta do NPC.

---

## 04/11/2026 — Implementação do sistema fuzzy

O arquivo `logica/fuzzy.py`, anteriormente utilizado como placeholder, passou a conter o sistema de inferência fuzzy do protótipo.

Foram definidas duas entradas.

### Entrada 1 — Necessidade de Assistência

Universo de discurso: 0–100.

Conjuntos linguísticos:

Baixa  
Média  
Alta

### Entrada 2 — Disposição Afetiva

Universo de discurso: 0–100.

Conjuntos linguísticos:

Hostil  
Neutro  
Amigável

### Saída — Nível de Assistência

Universo de discurso: 0–100.

Conjuntos linguísticos:

Nenhuma  
Genérica  
Intermediária  
Específica

Foram utilizadas funções de pertinência triangulares e trapezoidais.

O sistema atual utiliza inferência do tipo Mamdani.

Na execução das regras:

- o operador AND utiliza o mínimo;
- regras que produzem a mesma saída são agregadas pelo máximo;
- os conjuntos de saída são cortados de acordo com o grau de ativação;
- a agregação final utiliza o máximo;
- a defuzzificação utiliza o método do centroide.

Após a defuzzificação, o valor crisp é novamente avaliado nos conjuntos de saída. A categoria que possuir maior grau de pertinência é utilizada como decisão concreta do jogo.

Em caso de empate, é priorizada a categoria de menor assistência.

A base inicial possui nove regras, combinando os três níveis de Necessidade de Assistência com os três níveis de Disposição Afetiva.

A base de regras atual ainda será revisada posteriormente e deverá ser documentada explicitamente no formato linguístico SE–ENTÃO.

Foi identificado que regras futuras precisam preservar conscientemente o papel das duas entradas. Por exemplo, uma regra direta do tipo “SE a Necessidade for alta ENTÃO a dica será específica” poderia reduzir ou eliminar a influência da Disposição do NPC nessa região. Essa decisão deverá ser avaliada posteriormente.

---

## 04/11/2026 — Integração do fuzzy com as dicas

O sistema fuzzy foi integrado ao fluxo real do NPC.

As dicas da fase foram divididas em três bancos:

`DICAS_GENERICAS_FASE_1`

`DICAS_INTERMEDIARIAS_FASE_1`

`DICAS_ESPECIFICAS_FASE_1`

O botão comum “Dica” utiliza somente o banco de dicas genéricas.

O NPC, por outro lado, utiliza a categoria produzida pelo sistema fuzzy.

Quando a saída é:

Nenhuma → o NPC utiliza uma frase padrão de recusa.

Genérica → escolhe uma dica do conjunto genérico.

Intermediária → escolhe uma dica do conjunto intermediário.

Específica → escolhe uma dica do conjunto específico.

Foram também cadastradas respostas reutilizáveis para ausência de assistência, como:

“Não vou te dizer nada.”

“Você vai ter que se virar.”

“Humpf, descubra o caminho sozinho então.”

O fuzzy deixou de ser executado automaticamente no encontro. Ele passou a ser acionado somente quando o jogador efetivamente seleciona “Perguntar sobre as ilhas”.

---

## 04/11/2026 — Correções de apresentação

Durante os testes foi identificado que alguns identificadores internos dos estados ainda apareciam no modo Planejamento de Rota, por exemplo:

`q0`, `q1`, `q2`, `qf`.

Foi criada uma conversão entre o caminho interno do autômato e os nomes utilizados na interface.

Internamente:

`q0 → q2 → qf`

Visualmente:

`Ilha 1 → Ilha 3 → Ilha Final`

Os identificadores formais continuam sendo utilizados pelo motor do autômato, pelo histórico e pelos cálculos. Apenas a camada de apresentação utiliza os nomes das ilhas.

Mensagens de símbolos inválidos também foram ajustadas para apresentar o nome da ilha em vez do identificador interno do estado.

---

## 04/11/2026 — Bateria automatizada de testes

Foi criada uma estrutura específica de testes composta por:

`game/logica/testes_sistema.py`

e

`game/testes.rpy`.

A bateria automatizada passou a testar:

- normalização das métricas;
- cálculo da Necessidade de Assistência;
- saturação das métricas;
- monotonicidade da Necessidade de Assistência;
- histórico de estados;
- estados repetidos;
- limites da Disposição;
- impactos de todas as interações;
- classificação narrativa do NPC;
- validade das funções de pertinência;
- cobertura do universo fuzzy;
- casos de referência do sistema fuzzy;
- grade completa de combinações fuzzy;
- determinismo do autômato;
- sequências válidas;
- símbolos inválidos.

A grade fuzzy percorreu todas as combinações inteiras possíveis das duas entradas:

101 valores de Necessidade × 101 valores de Disposição = 10.201 combinações.

Resultado final da bateria:

- 43 testes aprovados;
- 0 falhas automáticas.

Também foi executado um diagnóstico de monotonicidade do valor crisp.

Foram observadas:

- 630 pequenas quedas numéricas ao aumentar a Necessidade de Assistência;
- 630 pequenas quedas numéricas ao aumentar a Disposição.

Essas quedas não foram classificadas automaticamente como erros, pois podem ocorrer devido à geometria resultante da sobreposição das funções de pertinência, da inferência Mamdani e da defuzzificação pelo centroide.

Foi então implementado um segundo diagnóstico mais importante para o comportamento concreto do jogo: verificar se essas oscilações poderiam provocar regressão na categoria de assistência.

Resultado:

- regressões de categoria ao aumentar a Necessidade: 0;
- regressões de categoria ao aumentar a Disposição: 0.

Portanto, apesar das pequenas oscilações no valor crisp, nenhuma delas fez o sistema reduzir o nível concreto de assistência.

Não foi observado comportamento como:

Específica → Intermediária

Intermediária → Genérica

Genérica → Nenhuma

como consequência do aumento de uma das entradas.

Com esse resultado, a implementação atual do núcleo foi considerada suficientemente estável para prosseguir para a próxima etapa de desenvolvimento.

---

# Estado do projeto ao final desta atualização

O protótipo possui atualmente um fluxo completo entre comportamento do jogador, estado interno do NPC e assistência adaptativa:

Navegação no autômato  
→ coleta das métricas do jogador  
→ cálculo da Necessidade de Assistência  
→ encontro com NPC  
→ geração da Disposição Afetiva  
→ interações alteram a Disposição  
→ jogador decide se solicita ajuda  
→ Necessidade é atualizada  
→ sistema fuzzy combina Necessidade + Disposição  
→ nível de assistência é calculado  
→ NPC recusa ou fornece dica genérica, intermediária ou específica.

O núcleo computacional principal encontra-se funcional.

---

# Próximas etapas definidas

A próxima etapa será construir uma arquitetura genérica para as fases posteriores.

O objetivo será permitir que cada fase seja definida principalmente por sua configuração, evitando replicação da lógica já implementada.

Entre os parâmetros que deverão variar por fase estão:

- autômato;
- textos introdutórios;
- bancos de dicas;
- limites de normalização;
- existência de armadilhas;
- chance de encontro com NPC;
- quantidade possível de encontros;
- mapa;
- elementos visuais específicos.

Após a arquitetura genérica, serão modelados os autômatos das sete fases.

A progressão deverá introduzir gradualmente novos comportamentos, utilizando representações lúdicas.

Exemplos já considerados incluem:

mais de um caminho possível até o destino;

redemoinhos representando loops e retornos;

prisão representando estados de armadilha;

combinações progressivamente mais complexas nas fases posteriores.

A Fase 1 atual poderá ser remodelada durante essa etapa.

Somente depois da definição estrutural das fases serão fixados parâmetros como chance de encontro com NPC, número máximo de encontros, limites de métricas e conteúdo definitivo das dicas.

Após a implementação das fases, serão realizados ajustes visuais e de identidade, incluindo backgrounds, botões, mapas específicos de cada fase, nome, ícone e símbolo do jogo.

Por fim será realizada uma nova bateria de testes e um teste final de integração do protótipo completo.

---

# Trabalhos futuros já reservados

Foram registrados como possibilidades fora do escopo atual:

- diferentes tipos de NPC;
- associação de NPCs mais hostis a categorias narrativas específicas, como piratas rivais ou integrantes da Marinha;
- associação de NPCs amigáveis a aliados, conhecidos ou grupos parceiros;
- memória persistente dos NPCs sobre encontros anteriores, eventos e ajudas;
- maior quantidade de opções de diálogo e interação;
- múltiplas dimensões afetivas;
- autômatos não determinísticos;
- seleção probabilística de categorias fuzzy;
- avaliação com usuários/alunos;
- animações e maior refinamento visual.

# Diário de Desenvolvimento — Atualização de 05/11 a 08/11/2026

## 05/11/2026 — Correções finais da bateria de testes e consolidação do núcleo

Após a criação da bateria automatizada de testes, foram identificados pequenos problemas exclusivamente no próprio código de testes, sem relação com a lógica principal do jogo.

Um dos problemas ocorreu na geração da representação legível dos caminhos do autômato. A variável `caminho_legivel` era utilizada em um teste antes de ter sido inicializada. O bloco de testes foi reorganizado para que cada sequência seja processada, convertida para nomes visíveis das ilhas e somente depois utilizada no relatório.

Também foi ajustada a forma de execução da bateria dentro do Ren'Py. A tentativa inicial de utilizar `jump executar_testes_sistema` diretamente a partir do menu principal resultava em erro porque o script Ren'Py não estava ativo naquele contexto. O sistema de testes foi então executado em contexto apropriado, permitindo a conclusão da bateria.

A bateria inicial apresentou:

- 43 testes aprovados;
- nenhuma falha automática.

Foram testadas, entre outras funcionalidades:

- normalização das métricas;
- cálculo da Necessidade de Assistência;
- saturação dos valores;
- monotonicidade da Necessidade de Assistência;
- histórico de estados;
- detecção de estados repetidos;
- limites da Disposição do NPC;
- impactos das interações;
- classificação narrativa da Disposição;
- funções de pertinência;
- cobertura do universo fuzzy;
- casos de referência do fuzzy;
- grade completa de combinações de entrada;
- processamento do autômato;
- detecção de símbolos inválidos;
- determinismo e completude do autômato.

### Diagnóstico da superfície fuzzy

Além dos testes binários de aprovação/falha, foi criada uma análise diagnóstica da superfície produzida pelo sistema fuzzy.

Foram examinadas todas as combinações inteiras entre:

- Necessidade de Assistência: 0–100;
- Disposição do NPC: 0–100.

Total:

101 × 101 = 10.201 combinações.

A primeira análise identificou:

- 630 pequenas quedas no valor crisp ao aumentar a Necessidade de Assistência;
- 630 pequenas quedas no valor crisp ao aumentar a Disposição.

Essas quedas não foram consideradas automaticamente como falha, pois o valor crisp resulta da geometria da agregação fuzzy e da defuzzificação pelo centroide.

Foi então criado um segundo diagnóstico, mais relevante para o comportamento do jogo: verificar se alguma dessas oscilações fazia a categoria final de assistência diminuir.

As categorias foram ordenadas como:

Nenhuma → Genérica → Intermediária → Específica.

Resultado:

- regressões de categoria ao aumentar Necessidade: 0;
- regressões de categoria ao aumentar Disposição: 0.

Portanto, apesar das oscilações numéricas do valor crisp, aumentar uma das entradas nunca produziu uma categoria concreta de ajuda inferior.

Com isso, o núcleo fuzzy atual foi considerado funcional para prosseguir com o desenvolvimento.

---

## 08/11/2026 — Início da generalização completa da arquitetura das fases

Com o núcleo funcional e testado, iniciou-se a transformação da Fase 1 em um modelo genérico que pudesse ser reutilizado pelas demais fases.

O objetivo principal passou a ser evitar duplicação de lógica. A intenção é que as futuras fases sejam definidas principalmente por configurações e conteúdo próprio, enquanto navegação, encontros, métricas, armadilhas e fuzzy permaneçam em motores comuns.

Foi estabelecida a seguinte separação conceitual:

### Arquivos `.rpy`

Responsáveis pelo comportamento ligado ao Ren'Py:

- fluxo do jogo;
- telas;
- botões;
- diálogos;
- menus;
- cenas;
- conteúdo narrativo;
- integração entre a interface e os módulos Python.

### Arquivos `.py`

Responsáveis pela lógica computacional:

- autômatos;
- transições;
- validações;
- métricas;
- Necessidade de Assistência;
- Disposição do NPC;
- funções fuzzy;
- configurações estruturais das fases.

Essa separação foi mantida como parte central da arquitetura do projeto.

---

# Generalização da configuração das fases

O arquivo `logica/automatos/fase_1.py` foi reorganizado para servir como modelo de configuração das próximas fases.

A configuração passou a possuir explicitamente:

- número da fase;
- nome da fase;
- alfabeto;
- estado inicial;
- estado final;
- estados de armadilha;
- nomes exibidos dos estados;
- função de transição;
- limites das métricas de assistência;
- configuração dos encontros com NPC.

A configuração do NPC passou a aceitar três modos:

- `nenhum`;
- `fixo`;
- `aleatorio`.

Também foram incluídos os parâmetros:

- `estado_fixo`;
- `chance_encontro`;
- `max_encontros`.

A Fase 1 atual continuou utilizando um encontro fixo, mas a estrutura passou a estar preparada para fases com encontros aleatórios.

---

# Generalização dos tipos de estado

O motor `automato.py` passou a reconhecer genericamente:

- estado inicial;
- estado final;
- estado de armadilha;
- estado intermediário.

Um estado intermediário é definido como um estado que não é:

- inicial;
- final;
- armadilha.

Essa definição passou a ser utilizada para determinar quais estados podem receber encontros aleatórios com NPC.

Foi mantida a decisão de que:

- estado inicial não pode conter NPC;
- estado final não pode conter NPC;
- estado de armadilha não pode conter NPC;
- somente ilhas intermediárias podem gerar encontros.

---

# Registro e validação genérica das fases

O arquivo `logica/fases.py` passou a funcionar como registro central das fases implementadas.

Somente fases efetivamente configuradas devem entrar no registro.

Neste momento:

- Fase 1 está registrada;
- Fases 2–7 ainda não estão registradas porque seus autômatos não foram definidos.

Foi criada uma rotina de validação estrutural para impedir que uma fase incorreta seja utilizada pelo jogo.

Entre as verificações implementadas:

- existência das chaves obrigatórias;
- existência do estado inicial;
- existência do estado final;
- exatamente um estado final por fase;
- validade dos estados de armadilha;
- impossibilidade de um estado ser simultaneamente final e armadilha;
- determinismo;
- completude;
- validade do alfabeto;
- inexistência de símbolos extras nas transições;
- validade dos destinos;
- validade dos limites das métricas;
- coerência entre existência de armadilha e ativação de sua métrica;
- validade da chance de encontro;
- validade do número máximo de encontros;
- coerência entre modo de NPC e número de encontros;
- validade da posição de NPC fixo;
- correspondência entre o número declarado pela fase e seu número no registro.

Durante essa etapa foi identificado um erro de ordem na validação: `max_encontros` era consultado antes de ter sido atribuído. A ordem do bloco foi corrigida para primeiro recuperar e validar o valor e somente depois utilizá-lo nas regras de coerência.

---

# Correção da seleção de fases

A tela de seleção de fases ainda utilizava uma estrutura antiga baseada em uma chave `implementada`.

Após a mudança para o novo registro central, a screen foi atualizada para utilizar:

`fases.fase_implementada(numero)`

A presença de uma fase no registro passou a indicar diretamente se ela está implementada.

A tela agora diferencia:

- fase bloqueada;
- fase desbloqueada, porém ainda em desenvolvimento;
- fase implementada e disponível.

A variável persistente:

`persistent.fase_max_desbloqueada`

continuou sendo utilizada para controlar a progressão.

O aviso visual apresentado pelo editor sobre essa propriedade não representa erro, pois atributos de `persistent` são criados dinamicamente pelo Ren'Py.

---

# Motor genérico de eventos dos estados

Foi criado o arquivo:

`eventos_estado.rpy`

Esse arquivo centraliza o comportamento executado quando o jogador chega a um novo estado.

A ordem atual de avaliação é:

estado final  
→ armadilha  
→ estado intermediário  
→ possível encontro com NPC.

Isso retirou da Fase 1 a responsabilidade de controlar manualmente seus eventos.

### Estados finais

Quando o estado atual é final:

- a fase é encerrada;
- a próxima fase é desbloqueada;
- o jogador retorna à seleção de fases.

### Estados de armadilha

Ao entrar em uma armadilha:

- `armadilhas_atingidas` é incrementado;
- a Necessidade de Assistência é recalculada;
- ocorre Game Over.

O jogador pode:

- Reiniciar;
- Voltar ao Menu.

Se escolher Reiniciar:

- `numero_resets` também é incrementado;
- a Necessidade é recalculada;
- o jogador retorna ao estado inicial.

Se escolher Menu:

- não é contabilizado um novo reinício.

Entrar novamente na mesma armadilha posteriormente contará como uma nova ocorrência.

---

# Generalização dos encontros com NPC

A aparição dos NPCs deixou de ser controlada diretamente pela Fase 1.

O arquivo `encontros_npc.rpy` passou a consultar a configuração da fase atual.

O sistema verifica:

1. se a fase possui NPC;
2. se o limite de encontros já foi atingido;
3. se o estado é intermediário;
4. se o encontro é fixo ou aleatório;
5. se o sorteio permite o encontro.

Para encontros aleatórios, a lógica utiliza:

`renpy.random.random()`

comparado à probabilidade configurada pela fase.

Ficou definido que:

- revisitar uma ilha pode gerar novo sorteio;
- o limite máximo de encontros continua valendo após reinício;
- sair da fase e entrar novamente zera o contador;
- cada encontro representa um Náufrago diferente;
- cada novo Náufrago recebe uma nova Disposição inicial.

---

# Generalização dos dois modos de jogo

A navegação passo a passo e o planejamento de rota foram adaptados para utilizar o mesmo motor de eventos.

No modo passo a passo:

transição  
→ registro das métricas  
→ atualização do estado  
→ exibição da ilha  
→ processamento dos eventos.

No modo Planejamento de Rota, foi realizada uma alteração estrutural importante.

Anteriormente uma sequência completa poderia ser processada diretamente.

O modo passou a percorrer cada símbolo individualmente.

Exemplo:

`ABBABA`

é processado estado a estado.

Dessa forma, eventos intermediários podem interromper corretamente a execução.

Por exemplo:

Ilha normal  
→ NPC  
→ continuação  
→ armadilha  
→ Game Over.

Ou:

Ilha normal  
→ estado final  
→ vitória imediata.

Isso garante que NPCs, armadilhas e vitória possuam o mesmo comportamento nos dois modos de jogo.

---

# Reorganização do fluxo entre fases

O `script.rpy` foi dividido conceitualmente em:

- início;
- seleção de fase;
- preparação da execução.

A preparação de uma fase passou a:

- carregar a configuração;
- validar o autômato;
- definir o estado inicial;
- zerar métricas;
- zerar dados de NPC;
- zerar dados fuzzy;
- preparar o conteúdo da fase;
- executar sua introdução;
- iniciar o modo selecionado.

Após a vitória, o jogador retorna à seleção de fases mantendo o modo atual.

---

# Generalização das dicas de NPC

Foi criado um sistema genérico para evitar repetição de dicas fornecidas por NPCs.

As dicas usadas são controladas separadamente por categoria:

- genérica;
- intermediária;
- específica.

Enquanto houver dicas não utilizadas naquela categoria, um NPC não repetirá uma dica já dada anteriormente por outro NPC.

Exemplo:

Banco específico:

A  
B  
C

Encontros:

NPC 1 → A  
NPC 2 → C  
NPC 3 → B

Após o esgotamento do banco, todas as dicas daquela mesma categoria voltam a ficar disponíveis.

A categoria decidida pelo fuzzy nunca é alterada por falta de dicas inéditas.

Assim:

Específica

não é substituída por:

Intermediária

quando seu banco é esgotado.

O Navegador e o NPC continuam podendo fornecer a mesma dica porque seus históricos são independentes.

---

# Generalização do conteúdo das fases

Foi criado um contrato comum para os arquivos:

`fases/fase_X.rpy`

Cada fase passa a possuir os labels:

- `fase_X_introducao`;
- `fase_X_preparar`;
- `fase_X_pedir_dica`;
- `fase_X_fornecer_dica_npc`;
- `fase_X_exibir_estado`.

Também possui três bancos:

- `DICAS_GENERICAS_FASE_X`;
- `DICAS_INTERMEDIARIAS_FASE_X`;
- `DICAS_ESPECIFICAS_FASE_X`.

A Fase 1 permanece com conteúdo funcional.

As Fases 2–7 receberam arquivos `.rpy` de scaffolding, contendo a mesma estrutura, porém com textos provisórios.

Os arquivos:

`logica/automatos/fase_2.py`

até:

`logica/automatos/fase_7.py`

permanecem vazios propositalmente até a definição dos autômatos.

---

# Despachante das fases

O arquivo:

`fases/despachante_fases.rpy`

passou a encaminhar genericamente:

- preparação;
- introdução;
- dica comum;
- dica de NPC;
- exibição visual do estado.

Isso permite que o restante da aplicação não precise saber qual conteúdo pertence a cada fase.

---

# Fortalecimento da validação

Antes de iniciar a criação dos seis novos autômatos, a validação foi reforçada.

O motor passou a rejeitar:

- símbolos de transição não pertencentes ao alfabeto;
- estados extras no dicionário de transições;
- múltiplos estados finais;
- armadilhas sem limite de métrica correspondente;
- métricas obrigatórias sem limites válidos;
- configuração incompleta do NPC;
- chances fora do intervalo 0–1;
- número máximo de encontros inválido;
- configuração incoerente entre modo de NPC e número de encontros;
- número interno de fase diferente do registro utilizado.

A bateria automatizada foi ampliada para testar também essas proteções.

---

# Resultado atual da bateria de testes

Após as novas validações:

- 47 testes aprovados;
- 0 falhas.

Os diagnósticos fuzzy permaneceram inalterados:

- 630 oscilações crisp ao aumentar Necessidade;
- 630 oscilações crisp ao aumentar Disposição;
- 0 regressões de categoria ao aumentar Necessidade;
- 0 regressões de categoria ao aumentar Disposição.

Portanto, a generalização da arquitetura não alterou o comportamento previamente validado do núcleo.

---

# Guia de arquitetura consolidado

Ao final dessa etapa foi consolidada a seguinte responsabilidade dos principais arquivos.

## `script.rpy`

Responsável por:

- entrada do jogo;
- seleção;
- preparação;
- inicialização de variáveis.

## `screens.rpy`

Responsável por:

- interface;
- botões;
- seleção de modo;
- seleção de fase;
- entrada de rota;
- controles de jogo.

## `navegacao.rpy`

Responsável por:

- execução dos dois modos;
- transições;
- registro dos percursos;
- integração com eventos dos estados.

## `eventos_estado.rpy`

Responsável por:

- reagir à chegada em estados;
- final;
- armadilha;
- NPC.

## `encontros_npc.rpy`

Responsável por:

- encontros;
- criação dos NPCs;
- interações;
- pedidos de ajuda;
- integração com fuzzy;
- seleção das dicas.

## `fases/fase_X.rpy`

Responsável pelo conteúdo específico:

- textos;
- falas;
- dicas;
- introdução;
- representação visual.

## `logica/automatos/fase_X.py`

Responsável pela configuração estrutural:

- estados;
- nomes das ilhas;
- transições;
- estado inicial;
- estado final;
- armadilhas;
- limites das métricas;
- configuração dos NPCs.

## `automato.py`

Motor genérico dos autômatos.

## `jogador.py`

Métricas e cálculo da Necessidade de Assistência.

## `npc.py`

Cálculo e atualização da Disposição Afetiva.

## `fuzzy.py`

Inferência fuzzy e seleção do nível de assistência.

## `fases.py`

Registro e validação das fases.

---

# Estado do desenvolvimento em 08/11/2026

A infraestrutura lógica genérica do jogo foi considerada concluída e validada.

O sistema possui atualmente:

- motor genérico de autômatos;
- validação estrutural das fases;
- dois modos de navegação;
- métricas do jogador;
- Necessidade de Assistência;
- encontros fixos e aleatórios;
- Disposição Afetiva;
- interações;
- sistema fuzzy;
- quatro níveis de assistência;
- controle de repetição das dicas;
- estados de armadilha;
- Game Over;
- progressão entre fases;
- scaffolding narrativo das sete fases;
- bateria automatizada de testes.

A próxima etapa deixa de ser a construção da infraestrutura e passa a ser a **modelagem efetiva das fases e dos autômatos**.

---

# Próxima etapa planejada

A intenção atual para a progressão é:

## Fase 1

Fase extremamente simples e introdutória.

A ideia inicial é utilizar um autômato essencialmente linear, permitindo ao jogador compreender o funcionamento básico da navegação.

## Fases 2–4

Devem introduzir progressivamente os elementos necessários para compreender e utilizar as mecânicas presentes no jogo.

Entre os elementos candidatos estão:

- caminhos alternativos;
- mais de uma possibilidade de rota;
- loops;
- retornos;
- armadilhas;
- maior número de estados.

Cada elemento novo deverá ser contextualizado por uma fala simples do Navegador no início da fase.

## Fases 5–7

Devem funcionar mais como desafios completos, combinando os elementos introduzidos anteriormente e exigindo que o jogador encontre rotas adequadas em estruturas progressivamente mais complexas.

Os autômatos ainda não foram definidos.

A próxima atividade será revisar o material utilizado na disciplina de Linguagens Formais e Autômatos e, a partir dele, desenhar os sete modelos.

Somente depois de desenhar cada autômato serão definidos, por fase:

- número de estados;
- transições;
- chance de encontro com NPC;
- limite máximo de encontros;
- presença de armadilhas;
- limites de normalização das métricas;
- dicas genéricas;
- dicas intermediárias;
- dicas específicas;
- texto introdutório;
- mapa.

---

# Etapas posteriores

Após a implementação das sete fases:

1. revisar explicitamente a base de regras fuzzy SE–ENTÃO;
2. executar novamente toda a bateria de testes;
3. realizar testes funcionais das sete fases;
4. iniciar o polimento visual;
5. substituir backgrounds temporários;
6. criar mapas definitivos;
7. ajustar botões e interface;
8. definir nome do jogo;
9. criar símbolo/logo;
10. criar ícone da aplicação;
11. configurar ícone exibido na janela/barra de tarefas;
12. gerar versão executável;
13. executar teste final de integração.

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
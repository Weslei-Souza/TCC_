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
- desenvolver testes sistemáticos e resultados.
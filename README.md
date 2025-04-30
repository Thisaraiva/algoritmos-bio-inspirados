# Participantes:
* João Antonio David
* Thiago de Freitas Saraiva

### Como rodar o programa:

Clonar o repositório e instalar as dependências:

```python
pip install flask numpy
```
Criar e rodar o ambiente local para que as dependências não gerem conflitos com as instalações globais do sistema operacional.

```python
# Criar ambiente virtual (substitua 'knapsack_env' pelo nome que preferir)
python -m venv knapsack_env

# Ativar o ambiente virtual

# Windows:
'knapsack_env\Scripts\activate'
```


# Relatório de Resultados - Knapsack Problem Solver

## Introdução

Este relatório apresenta os resultados obtidos com a implementação de cinco algoritmos bioinspirados (Algoritmo Genético, Otimização por Colônia de Formigas, Otimização por Enxame de Partículas, Busca do Cuco e Algoritmo dos Vagalumes) para resolver o Problema da Mochila (Knapsack Problem). O sistema foi desenvolvido em Python utilizando Flask para a interface web e bibliotecas como NumPy para cálculos numéricos. A interface web permite ao usuário configurar os itens (pesos e valores), a capacidade da mochila e o algoritmo desejado.

O objetivo é comparar o desempenho dos algoritmos em um conjunto de dados com 50 itens gerados aleatoriamente e uma capacidade de mochila de 50 unidades. Este relatório descreve o funcionamento dos algoritmos, apresenta exemplos de entrada e saída, e discute as dificuldades enfrentadas e os aprendizados adquiridos durante o desenvolvimento.

## Funcionamento dos Algoritmos

Os cinco algoritmos implementados são baseados em técnicas bioinspiradas e foram adaptados para resolver o Problema da Mochila, que consiste em selecionar um subconjunto de itens que maximize o valor total sem exceder a capacidade da mochila. Abaixo está uma descrição de cada algoritmo:

### 1. Algoritmo Genético (GA)

**Funcionamento:** Simula a evolução biológica por meio de uma população de soluções (indivíduos) que passam por seleção, cruzamento e mutação. Cada indivíduo é uma sequência binária indicando quais itens são incluídos na mochila.
**Parâmetros:** Tamanho da população (50), número de gerações (100), taxa de mutação (0.1).
**Processo:**
1. Inicializa uma população aleatória de soluções válidas.
2. Avalia a aptidão (valor total dos itens, zero se exceder a capacidade).
3. Seleciona pais com base na aptidão (torneio com 3 candidatos).
4. Realiza cruzamento (crossover de um ponto) e mutação (inversão de bits com probabilidade).
5. Atualiza a população e mantém a melhor solução.

### 2. Otimização por Colônia de Formigas (ACO)

**Funcionamento:** Inspirado no comportamento de formigas que depositam feromônios em caminhos. Cada formiga constrói uma solução escolhendo itens com base em feromônios e uma heurística (valor/peso).
**Parâmetros:** Número de formigas (20), iterações (100), alpha (1), beta (2), taxa de evaporação (0.5), q0 (0.9).
**Processo:**
1. Inicializa trilhas de feromônios uniformemente.
2. Cada formiga constrói uma solução escolhendo itens probabilisticamente (influenciada por feromônios e heurística).
3. Atualiza os feromônios com base nas melhores soluções, aplicando evaporação para evitar convergência prematura.
4. Mantém a melhor solução encontrada.

### 3. Otimização por Enxame de Partículas (PSO)

**Funcionamento:** Inspirado no movimento de enxames, onde partículas (soluções) ajustam suas posições com base em sua melhor posição histórica e na melhor posição global.
**Parâmetros:** Número de partículas (30), iterações (100), inércia (0.7), coeficientes cognitivos e sociais (1.5).
**Processo:**
1. Inicializa partículas com posições e velocidades aleatórias.
2. Converte posições em soluções binárias (limiar de 0.5) e repara soluções inválidas.
3. Atualiza velocidades com base na inércia, melhor posição pessoal e global.
4. Ajusta posições e mantém a melhor solução.

### 4. Busca do Cuco (CS)

**Funcionamento:** Baseado no comportamento de cucos que depositam ovos em ninhos alheios. Cada ninho representa uma solução, e novos ninhos são gerados via caminhada de Lévy.
**Parâmetros:** Número de ninhos (25), iterações (100), probabilidade de descoberta (0.25).
**Processo:**
1. Inicializa ninhos com soluções aleatórias.
2. Gera novos ninhos via caminhada de Lévy e substitui ninhos piores se a nova solução for melhor.
3. Descarta uma fração dos ninhos piores e substitui por novos.
4. Mantém a melhor solução encontrada.

### 5. Algoritmo dos Vagalumes (FA)

**Funcionamento:** Inspirado na atração de vagalumes por luz. Cada vagalume representa uma solução, e a intensidade (aptidão) determina o movimento.
**Parâmetros:** Número de vagalumes (25), iterações (100), alpha (0.2), beta0 (1), gamma (1).
**Processo:**
1. Inicializa vagalumes com posições aleatórias.
2. Calcula a intensidade (valor da solução após reparo).
3. Move vagalumes em direção a outros com maior intensidade, ajustando posições com um termo aleatório.
4. Mantém a melhor solução.

## Exemplo de Entrada e Saída

### Entrada

Os testes foram realizados com um conjunto de 50 itens gerados aleatoriamente, com a capacidade da mochila fixada em 50 unidades. Abaixo está a lista de itens (pesos e valores):

| Item    | Peso | Valor |
|---------|------|-------|
| Item 1  | 94   | 14    |
| Item 2  | 22   | 96    |
| ...     | ...  | ...   |
| Item 49 | 66   | 50    |
| Item 50 | 98   | 19    |

**Capacidade da Mochila:** 50

### Saída

Os resultados para cada algoritmo são apresentados abaixo, incluindo a solução (itens incluídos), valor total e peso total.

#### Algoritmo Genético (GA)

**Solução:** Itens 17, 29, 30, 35, 42, 48
**Valor Total:** 325
**Peso Total:** 49
**Itens Selecionados:**
- Item 17: Peso 2, Valor 52
- Item 29: Peso 8, Valor 56
- Item 30: Peso 16, Valor 49
- Item 35: Peso 7, Valor 66
- Item 42: Peso 15, Valor 100
- Item 48: Peso 1, Valor 2

#### Otimização por Colônia de Formigas (ACO)

**Solução:** Itens 9, 17, 29, 35, 42, 48
**Valor Total:** 343
**Peso Total:** 50
**Itens Selecionados:**
- Item 9: Peso 17, Valor 67
- Item 17: Peso 2, Valor 52
- Item 29: Peso 8, Valor 56
- Item 35: Peso 7, Valor 66
- Item 42: Peso 15, Valor 100
- Item 48: Peso 1, Valor 2

#### Otimização por Enxame de Partículas (PSO)

**Solução:** Itens 2, 24, 48
**Valor Total:** 115
**Peso Total:** 39
**Itens Selecionados:**
- Item 2: Peso 22, Valor 96
- Item 24: Peso 16, Valor 17
- Item 48: Peso 1, Valor 2

#### Busca do Cuco (CS)

**Solução:** Item 27
**Valor Total:** 17
**Peso Total:** 15
**Itens Selecionados:**
- Item 27: Peso 15, Valor 17

#### Algoritmo dos Vagalumes (FA)

**Solução:** Item 16
**Valor Total:** 78
**Peso Total:** 28
**Itens Selecionados:**
- Item 16: Peso 28, Valor 78

## Análise dos Resultados

### Comparação de Desempenho

- **Otimização por Colônia de Formigas (ACO)** obteve o melhor resultado, com um valor total de 343 e peso total de 50, utilizando a capacidade máxima da mochila.
- **Algoritmo Genético (GA)** teve um desempenho próximo ao ACO, com valor total de 325 e peso total de 49, indicando uma solução quase ótima.
- **Otimização por Enxame de Partículas (PSO)** apresentou um desempenho inferior, com valor total de 115 e peso total de 39, não utilizando toda a capacidade disponível.
- **Busca do Cuco (CS)** teve o pior desempenho, selecionando apenas um item (valor 17, peso 15), sugerindo convergência prematura ou configuração inadequada.
- **Algoritmo dos Vagalumes (FA)** também apresentou resultado fraco, selecionando apenas um item (valor 78, peso 28), indicando dificuldades em explorar o espaço de busca.

### Observações

- Algoritmos baseados em populações maiores e exploração diversificada (ACO e GA) superaram os demais, provavelmente devido à sua capacidade de balancear exploração e explotação.
- PSO, CS e FA parecem ter convergido para soluções locais, selecionando poucos itens e deixando capacidade ociosa.
- A escolha de itens com alta relação valor/peso (como o Item 42, valor 100, peso 15) foi mais frequente em ACO e GA, indicando uma boa heurística nesses algoritmos.

## Dificuldades Enfrentadas

### Configuração de Parâmetros

- Ajustar os parâmetros (e.g., taxa de mutação, evaporação de feromônios, coeficientes do PSO) foi desafiador, pois valores inadequados levaram a convergência prematura ou soluções ruins.
- CS e FA apresentaram resultados muito abaixo do esperado, sugerindo que os parâmetros padrão (número de ninhos, alpha, gamma) não são ideais para este problema.

### Convergência Prematura

- CS e FA frequentemente convergiram para soluções com poucos itens, indicando que os mecanismos de exploração (caminhada de Lévy e movimento dos vagalumes) não foram eficazes para este conjunto de dados.

### Escalabilidade

- Com 50 itens, o tempo de execução foi aceitável, mas algoritmos como ACO e GA podem se tornar lentos para instâncias maiores devido ao número de iterações e cálculos.

### Interface Web

- Garantir que a interface fosse responsiva e lidasse com entradas inválidas (e.g., pesos negativos) exigiu validações adicionais no JavaScript e no backend.

### Debugging

- Erros iniciais em PSO e FA foram causados por soluções inválidas (excedendo a capacidade), resolvidos com funções de reparo, mas isso adicionou complexidade ao código.

## Aprendizados

### Compreensão dos Algoritmos Bioinspirados

- A implementação prática aprofundou o entendimento sobre como os algoritmos exploram o espaço de busca e lidam com restrições (como a capacidade da mochila).
- ACO e GA mostraram-se robustos para problemas combinatórios, enquanto CS e FA requerem ajustes cuidadosos para evitar armadilhas locais.

### Importância dos Parâmetros

- A experimentação com diferentes configurações destacou a sensibilidade dos algoritmos a parâmetros, incentivando a leitura de literatura para escolhas informadas.

### Desenvolvimento Web com Flask

- A integração de algoritmos Python com uma interface web via Flask foi um aprendizado valioso, especialmente na comunicação assíncrona com AJAX.

### Resolução de Problemas

- Lidar com erros como soluções inválidas e convergência prematura reforçou a importância de testes sistemáticos e validação de resultados.

### Análise Comparativa

- Comparar os algoritmos revelou que não existe uma solução universal; o desempenho depende do problema e da configuração.

## Conclusão

O projeto demonstrou a aplicação de algoritmos bioinspirados ao Problema da Mochila, com a Otimização por Colônia de Formigas (ACO) alcançando o melhor resultado (valor 343) e a Busca do Cuco (CS) apresentando o pior (valor 17). A interface web facilitou a interação com o sistema, permitindo testes com diferentes configurações. As principais dificuldades incluíram a configuração de parâmetros e a convergência prematura de alguns algoritmos, enquanto os aprendizados abrangeram desde a implementação prática até a integração com tecnologias web.

### Para melhorias futuras, recomenda-se:

- Ajustar os parâmetros de CS e FA com base em testes adicionais.
- Implementar gráficos de convergência para visualizar o desempenho ao longo das iterações.
- Testar os algoritmos com diferentes tamanhos de entrada para avaliar escalabilidade.
- Adicionar validações mais robustas na interface para evitar entradas inválidas.

Este projeto foi uma oportunidade valiosa para combinar conceitos de otimização, programação e desenvolvimento web, resultando em um sistema funcional e educativo.
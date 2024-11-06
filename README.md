# Trabalho 1 - Inteligência Artificial

Participantes: Matheus Alves e Pablo Sousa

## Contextualização

O trabalho apresentado tem como objetivo implementar e comparar o desempenho de dois algoritmos de busca não informada aplicados ao problema clássico de labirinto. A atividade visa avaliar aspectos de desempenho como tempo de execução, consumo de memória, completude e optimalidade dos algoritmos escolhidos. A partir desses resultados, busca-se analisar e discutir por que determinados algoritmos apresentam vantagens em certas métricas e condições do problema, oferecendo uma compreensão mais profunda das técnicas de busca na área de Inteligência Artificial.

---

## 1. Implementação

Para resolver o problema de busca por um caminho em uma matriz com movimentos de salto de duas casas, foram implementados os algoritmos de **Busca em Largura (BFS)** e **Busca em Profundidade (DFS)**. Cada célula da matriz representa um nó, e os movimentos possíveis (esquerda, direita, cima, baixo) com salto de duas casas representam as arestas. Abaixo uma breve descrição de cada algoritmo:

- **BFS**: Explora o grafo em largura, visitando todos os vizinhos de um nó antes de avançar para o próximo nível. Isso garante que o primeiro caminho encontrado é o mais curto em termos de movimentos, sendo ótimo em grafos não ponderados.
  
- **DFS**: Explora o grafo em profundidade, tentando avançar o máximo possível por um caminho antes de retroceder. DFS não garante o menor caminho, mas é útil para explorar todas as rotas possíveis. Em termos de memória, DFS geralmente utiliza menos espaço em grafos grandes.

---

## 2. Medições de Desempenho

Para avaliar os algoritmos, foram medidas as seguintes métricas:
- **Tempo de Execução**: Eficiência do algoritmo em termos de velocidade.
- **Consumo de Memória**: Memória usada para armazenar dados durante a execução.
- **Completude**: Habilidade do algoritmo de sempre encontrar um caminho, se ele existir.
- **Optimalidade**: Verifica se o algoritmo encontra o menor caminho.

### Resultados das Medições:

#### BFS
- **Tempo de Execução**: 0.001003 segundos
- **Consumo de Memória**: 4.55 KB
- **Completude**: O algoritmo é completo (sempre encontra o caminho se existir)
- **Optimalidade**: O caminho encontrado é o menor possível

#### DFS
- **Tempo de Execução**: 0.000000 segundos
- **Consumo de Memória**: 0.80 KB
- **Completude**: O algoritmo é completo (se existir caminho, ele encontrará)
- **Optimalidade**: DFS não garante a melhor solução (menor caminho)

---

## 3. Resultados e Análise Comparativa

| Métrica             | BFS                   | DFS                    |
|---------------------|-----------------------|------------------------|
| Tempo de Execução   | 0.001003 segundos     | 0.000000 segundos      |
| Consumo de Memória  | 4.55 KB               | 0.80 KB                |
| Completude          | Completo              | Completo               |
| Optimalidade        | Ótimo (menor caminho) | Não garante menor caminho |

### Análise dos Resultados

1. **Tempo de Execução**:
   - O DFS apresentou menor tempo de execução, pois explora diretamente até o fim sem verificar todas as alternativas antes de avançar. Isso é vantajoso em problemas pequenos ou quando o caminho está próximo do ponto de partida.
   - O BFS, por sua vez, verifica cada nível em largura, o que o torna um pouco mais lento, mas garante o menor caminho.

2. **Consumo de Memória**:
   - O DFS usou menos memória que o BFS, pois mantém apenas o caminho atual e nós visitados. 
   - O BFS mantém todos os nós do nível atual na fila, aumentando o uso de memória, especialmente em grafos grandes.

3. **Completude**:
   - Ambos são completos para o problema, ou seja, encontram um caminho, se houver, da posição inicial até a final.

4. **Optimalidade**:
   - O BFS é ótimo e encontra o menor caminho em termos de passos, ideal para problemas de menor caminho.
   - O DFS não garante optimalidade e pode encontrar caminhos mais longos.

### Discussão do Desempenho em Diferentes Condições

- **Problemas de Menor Caminho**: O BFS é preferível para encontrar o menor caminho em grafos não ponderados.
  
- **Limitação de Recursos de Memória**: O DFS é ideal para situações de baixa memória ou quando queremos uma exploração completa do grafo sem precisar do menor caminho.
  
- **Exploração Completa**: Em cenários onde é necessário explorar todos os caminhos, o DFS é vantajoso pelo menor consumo de memória.

---

## 4. Conclusão e Sugestões de Melhorias

Ambos os algoritmos foram eficazes, mas apresentaram vantagens e desvantagens específicas:

- **BFS** é ideal para encontrar o menor caminho em grafos não ponderados, mas consome mais memória.
  
- **DFS** apresentou menor consumo de memória e tempo de execução ligeiramente melhor no exemplo dado, mas não garante optimalidade.

### Sugestões de Melhoria:
1. **Algoritmos Heurísticos (A\*)**: Implementar o A* para combinar menor caminho e menor uso de memória.
2. **Busca Limitada em Profundidade**: Uma variante de DFS com limite de profundidade pode reduzir o tempo e evitar caminhos muito longos.
3. **Memória Auxiliar para DFS**: Usar uma pilha iterativa com limite de profundidade pode controlar o consumo de memória em DFS.

Em resumo, ambos são úteis em diferentes contextos, e a escolha depende das necessidades de completude, optimalidade e tamanho do problema.

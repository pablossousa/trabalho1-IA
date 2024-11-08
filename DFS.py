from collections import deque
import time
import tracemalloc

matriz = [
    ['A', 0, 'B', 1, 'C', 0, 'D', 0, 'E'],
    [0, 0, 1, 0, 0, 0, 1, 0, 0],
    ['F', 0, 'G', 0, 'H', 0, 'I', 1, 'J'],
    [1, 0, 1, 0, 1, 0, 0, 0, 1],
    ['K', 1, 'L', 0, 'M', 0, 'N', 0, 'O'],
    [0, 0, 0, 0, 0, 0, 1, 0, 1],
    ['P', 1, 'Q', 1, 'R', 0, 'S', 0, 'T'],
    [0, 0, 0, 0, 1, 0, 1, 0, 0],
    ['U', 0, 'V', 0, 'X', 0, 'Y', 0, 'Z']
]

inicio = (8, 0)
fim = (0, 8)
movimentos = [(-2, 0), (2, 0), (0, -2), (0, 2)]

def movimento_possivel(x, y, dx, dy):
    meio_x, meio_y = x + dx // 2, y + dy // 2
    destino_x, destino_y = x + dx, y + dy
    if 0 <= meio_x < len(matriz) and 0 <= meio_y < len(matriz[0]) and \
       0 <= destino_x < len(matriz) and 0 <= destino_y < len(matriz[0]):
        if matriz[meio_x][meio_y] != 1 and matriz[destino_x][destino_y] != 1:
            return True
    return False

def busca_profundidade(matriz, posicao, fim, visitados, caminho):
    x, y = posicao
    if posicao == fim:
        return caminho
    
    visitados.add(posicao)
    for dx, dy in movimentos:
        novo_x, novo_y = x + dx, y + dy
        if movimento_possivel(x, y, dx, dy) and (novo_x, novo_y) not in visitados:
            resultado = busca_profundidade(matriz, (novo_x, novo_y), fim, visitados, caminho + [(novo_x, novo_y)])
            if resultado: 
                return resultado

    visitados.remove(posicao)
    return None 

def executar_busca_profundidade(matriz, inicio, fim):
    inicio_tempo = time.time()
    tracemalloc.start()
  
    caminho = busca_profundidade(matriz, inicio, fim, set(), [inicio])
    
    memoria_usada, _ = tracemalloc.get_traced_memory()
    tempo_execucao = time.time() - inicio_tempo
    tracemalloc.stop()

    if caminho:
        print("Caminho encontrado:")
        for passo in caminho:
            print(passo)
        print("\nMétricas de desempenho:")
        print(f"Tempo de Execução: {tempo_execucao:.6f} segundos")
        print(f"Consumo de Memória: {memoria_usada / 1024:.2f} KB")
        print("Completude: Algoritmo completo se existir caminho")
        print("Optimalidade: DFS não garante o menor caminho")
    else:
        print("Nenhum caminho encontrado entre os pontos.")
        print("Completude: Algoritmo completo, mas nenhum caminho existe entre os pontos.")

executar_busca_profundidade(matriz, inicio, fim)

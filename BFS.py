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

def movimento_valido(x, y, dx, dy):
    inter_x, inter_y = x + dx // 2, y + dy // 2
    dest_x, dest_y = x + dx, y + dy

    if 0 <= inter_x < len(matriz) and 0 <= inter_y < len(matriz[0]) and \
       0 <= dest_x < len(matriz) and 0 <= dest_y < len(matriz[0]):
        if matriz[inter_x][inter_y] != 1 and matriz[dest_x][dest_y] != 1:
            return True
    return False

def busca_bfs(matriz, inicio, fim):
    inicio_tempo = time.time()
    tracemalloc.start()

    fila = deque([(inicio, [inicio])])
    visitados = set([inicio])

    while fila:
        (x, y), caminho = fila.popleft()
        
        if (x, y) == fim:
            tempo_execucao = time.time() - inicio_tempo
            memoria_usada, _ = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            print("Caminho encontrado:")
            for passo in caminho:
                print(passo)
            print("\nMétricas de desempenho:")
            print(f"Tempo de Execução: {tempo_execucao:.6f} segundos")
            print(f"Consumo de Memória: {memoria_usada / 1024:.2f} KB")
            print("O algoritmo é completo e o caminho encontrado é o menor possível.")
            return

        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy
            if movimento_valido(x, y, dx, dy) and (nx, ny) not in visitados:
                visitados.add((nx, ny))
                fila.append(((nx, ny), caminho + [(nx, ny)]))

    print("Nenhum caminho encontrado entre os pontos.")
    print("O algoritmo é completo, mas não existe caminho disponível entre os pontos.")

busca_bfs(matriz, inicio, fim)

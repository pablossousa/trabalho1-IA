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


start = (8, 0)  
end = (0, 8) 


movimentos = [(-2, 0), (2, 0), (0, -2), (0, 2)]


def movimento_valido(x, y, dx, dy):
    inter_x, inter_y = x + dx // 2, y + dy // 2
    dest_x, dest_y = x + dx, y + dy
    
    if 0 <= inter_x < len(matriz) and 0 <= inter_y < len(matriz[0]) and \
       0 <= dest_x < len(matriz) and 0 <= dest_y < len(matriz[0]):
        
        if matriz[inter_x][inter_y] != 1 and matriz[dest_x][dest_y] != 1:
            return True
    return False


def bfs(matriz, start, end):
    
    start_time = time.time()
    tracemalloc.start()

    fila = deque([(start, [start])])
    visitado = set([start])
    caminho_otimo = None 
    
    while fila:
        (x, y), caminho = fila.popleft()
        
        if (x, y) == end:
            caminho_otimo = caminho 
            break
        
        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy
            if movimento_valido(x, y, dx, dy) and (nx, ny) not in visitado:
                visitado.add((nx, ny))
                fila.append(((nx, ny), caminho + [(nx, ny)]))
    

    memoria_usada, _ = tracemalloc.get_traced_memory()
    tempo_execucao = time.time() - start_time
    tracemalloc.stop()


    if caminho_otimo:
        print("Caminho encontrado:")
        for pos in caminho_otimo:
            print(pos)
        print("\nMétricas de desempenho:")
        print(f"Tempo de Execução: {tempo_execucao:.6f} segundos")
        print(f"Consumo de Memória: {memoria_usada / 1024:.2f} KB")
        print("Completude: O algoritmo é completo (sempre encontra o caminho se existir)")
        print("Optimalidade: O caminho encontrado é o menor possível")
    else:
        print("Nenhum caminho encontrado de U até E.")
        print("\nCompletude: O algoritmo é completo, mas nenhum caminho existe entre U e E.")


bfs(matriz, start, end)
from collections import deque
import time
import tracemalloc

from config import matriz, inicio, fim, movimentos
from funcoes import movimento_valido, exibir_caminho, exibir_medicoes

def busca_bfs(matriz, inicio, fim, movimentos):

    inicio_tempo = time.time()
    tracemalloc.start()

    fila = deque([(inicio, [inicio])])
    visitados = set([inicio])

    while fila:
        atual, caminho = fila.popleft()
        x, y = atual

        if atual == fim:
            tempo_execucao = time.time() - inicio_tempo
            memoria_usada, _ = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            exibir_caminho(caminho)
            exibir_medicoes(tempo_execucao, memoria_usada)
            return

        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy
            destino = (nx, ny)

            if movimento_valido(matriz, atual, destino) and destino not in visitados:
                visitados.add(destino)
                fila.append((destino, caminho + [destino]))

    print("Nenhum caminho encontrado.")
    tracemalloc.stop()

busca_bfs(matriz, inicio, fim, movimentos)

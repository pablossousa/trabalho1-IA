def movimento_valido(matriz, atual, destino):
    x, y = atual
    nx, ny = destino

    if not (0 <= nx < len(matriz) and 0 <= ny < len(matriz[0])):
        return False

    inter_x = (x + nx) // 2
    inter_y = (y + ny) // 2

    if matriz[inter_x][inter_y] == 1:
        return False

    if matriz[nx][ny] == 1:
        return False

    return True

def exibir_caminho(caminho):
    for passo in caminho:
        print(f"{passo}")

def exibir_medicoes(tempo_execucao, memoria_usada):
    print("\nMétricas de desempenho:")
    print(f"Tempo de Execução: {tempo_execucao:.6f} segundos")
    print(f"Consumo de Memória: {memoria_usada / 1024:.2f} KB")

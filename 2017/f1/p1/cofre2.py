def main():
    n, m = map(int, input().split())
    cofre = list(map(int, input().split()))
    etapas = list(map(int, input().split()))
    resultado = [0] * 10

    # Contar o primeiro elemento (posição inicial = 1)
    resultado[cofre[etapas[0] - 1]] += 1

    for i in range(1, m):
        origem = etapas[i - 1]
        destino = etapas[i]

        passo = 1 if destino > origem else -1
        for pos in range(origem + passo, destino + passo, passo):
            resultado[cofre[pos - 1]] += 1

    print(*resultado)

if __name__ == "__main__":
  main()

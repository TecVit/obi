def main():
    n, m = map(int, input().split())
    matriz = [list(map(int, input().split())) for _ in range(n)]

    menor_x = -1  # posição do primeiro número não-zero mais à esquerda até agora

    for i in range(n):
        x = m  # começa com o máximo
        for j in range(m):
            if matriz[i][j] != 0:
                x = j
                break

        # Linha toda zero
        if x == m:
            for k in range(i + 1, n):
                if any(matriz[k][c] != 0 for c in range(m)):
                    print("N")
                    return
            break  # tudo abaixo é zero, podemos sair
        else:
            if x < menor_x:
                print("N")
                return
            menor_x = x
            # Checar colunas da 0 até x nas linhas abaixo
            for k in range(i + 1, n):
                if any(matriz[k][c] != 0 for c in range(x + 1)):
                    print("N")
                    return

    print("S")

if __name__ == "__main__":
  main()
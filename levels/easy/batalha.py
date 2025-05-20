def main():
    a1 = int(input())
    d1 = int(input())
    a2 = int(input())
    d2 = int(input())

    # Vida do 1 = a2 - d1
    # Se for a2 <= d1 ele esta vivo
    # E se o a1 > d2 o 2 esta morto

    jogador1_desmaia = d1 != a2
    jogador2_desmaia = d2 != a1

    # Determina o resultado
    if not jogador1_desmaia and jogador2_desmaia:
        print(1)
    elif not jogador2_desmaia and jogador1_desmaia:
        print(2)
    else:
        print(-1)


if __name__ == "__main__":
    main()
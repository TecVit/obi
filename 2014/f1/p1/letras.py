def main():
    letra = str(input())
    palavras = [[letra for letra in palavra] for palavra in input().split()]
    c = 0

    for palavra in palavras:
        if palavra.count(letra) > 0:
            c += 1

    print(f"{((c / len(palavras))*100):.1f}")

if __name__ == "__main__":
    main()

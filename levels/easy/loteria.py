def main():
    apostas = set(map(int, input().split()))
    resultado = set(map(int, input().split()))

    prints = ['azar', 'azar', 'azar', 'terno', 'quadra', 'quina', 'sena']

    print(prints[len(apostas & resultado)]);
    return 0

if __name__ == "__main__":
    main()
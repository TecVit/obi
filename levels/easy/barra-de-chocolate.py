def main():
    n = int(input()) # Número de divisões
    ns = list(map(int, input().split())) # Pedaços depois de cada divisão

    print(sum(ns) - n)

if __name__ == "__main__":
    main()
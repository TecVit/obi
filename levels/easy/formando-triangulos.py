def maior_triangulo(tamanho, possivel):
    possivel.sort(reverse=True)

    for i in range(tamanho - 2):
        a, b, c = possivel[i], possivel[i+1], possivel[i+2]
        if b + c > a:
            return sorted([a, b, c])
        
    return []

def main():
    n = int(input())
    palitos = list(map(int, input().split()))

    resultado = maior_triangulo(n, palitos)
    print(*resultado)

if __name__ == "__main__":
    main()
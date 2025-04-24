def trocarSentido(sentido):
    return 0 if sentido == 1 else 1

def main():
    n = int(input())
    m = [['f'] * (n + 2) for _ in range(n + 2)]
    m[0] = [['f'] * (n + 2)]

    for i in range(1, n + 1):
        row = input()
        row = 'f' + row + 'f'

        for j in range(n + 2):
            m[i][j] = row[j]
        
    max_moedas = float("-inf")
    moedas = 0

    y, x = 1, 1
    s = 0
    c = 0

    # 0 => Direita
    # 1 => Esquerda
    
    while c < n ** 2:
        c += 1

        prox = 0
        if s == 0:
            prox = m[y][x+1]
        elif s == 1:
            prox = m[y][x-1]
        
        if m[y][x] == 'o':
            moedas += 1
        elif m[y][x] == 'A':
            moedas = 0

        if moedas > max_moedas:
            max_moedas = moedas
        
        if prox == 'f':
            y += 1
            s = trocarSentido(s)
            continue
        else:
            x += 1 if s == 0 else -1

    print(max_moedas)

if __name__ == "__main__":
    main()

def main():
    n = int(input())
    fs = [1]

    index_menor = -1

    c = 0
    t = 0

    for i in range(1, min(n, 18)):
        fat = i * fs[i-1]
        fs.append(fat)

        if fat > n and index_menor == -1:
            index_menor = i-1

    while t != n:
        if t + fs[index_menor] > n:
            index_menor -= 1
            continue

        t += fs[index_menor]    
        c += 1

    print(c)

if __name__ == "__main__":
    main()
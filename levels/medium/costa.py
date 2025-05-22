def main():
    rows, columns = map(int, input().split())
    mapa = [['.'] * (columns + 2)]
    
    for i in range(rows):
        row = str(input())
        row = '.' + row + '.'
        mapa.append([str(x) for x in row])

    mapa.append(['.'] * (columns + 2))

    c = 0
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            p = mapa[i][j]

            t = mapa[i-1][j]
            b = mapa[i+1][j]
            r = mapa[i][j+1]
            l = mapa[i][j-1]

            list = [t, b, r, l]
            
            if p == '#' and list.count("#") <= 3:
                c += 1 

    # for row in mapa:
    #     print(row)

    print(c)

    return 0

if __name__ == "__main__":
    main()
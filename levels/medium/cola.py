def main():
    n = int(input())

    rs = []

    for _ in range(n):
        r = input().strip()
        rs.append(r)

    f = {}

    for r in rs:
        if r in f:
            f[r] += 1
        else:
            f[r] = 1

    c = 0
    for r in rs:
        if f[r] > 1:
            c += 1

    print(c)
    return 0

if __name__ == "__main__":
    main()
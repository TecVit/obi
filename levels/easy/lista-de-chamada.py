def main():
    n, k = map(int, input().split())
    ps = []

    for i in range(n):
        p = str(input())
        ps.append(p)

    ps.sort()

    print(ps[k-1])

    return 0

if __name__ == "__main__":
    main()
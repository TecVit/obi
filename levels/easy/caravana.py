def main():
    n = int(input())
    ns = [int(input()) for _ in range(n)]

    m = int(sum(ns) / n)

    for i in range(n):
        a = ns[i]
        print((m - a))

    return 0

if __name__ == "__main__":
    main()
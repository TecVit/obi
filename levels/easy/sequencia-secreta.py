def main():
    n = int(input())
    ns = list(int(input()) for _ in range(n))

    c = 1
    a = 1

    for i in range(1, n):
        x = ns[i]
        if x == a:
            continue
        else:
            a = x
            c += 1

    print(c)
    
    return 0

if __name__ == "__main__":
    main()
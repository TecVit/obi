def main():
    p, n = map(int, input().split())
    ns = list(map(int, input().split()))
    ns.sort(reverse=True)

    print(ns)
    
    for n in ns:
        print(p + n)
        if p + n > 100 or p + n < 0:
            continue
        p += n

    print(p)
    return 0

if __name__ == "__main__":
    main()
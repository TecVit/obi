def main():
    n = int(input())
    ns = list(map(int, input().split()))
    
    a, r = 0, 0
    for n in ns:
        if n != a:
            a = n
            r += 1

    print(r)

if __name__ == "__main__":
    main()
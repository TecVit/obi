def main():
    n = int(input())
    d = int(input())

    r = n // d

    if n % d == 0:
        for _ in range(d):
            print(r)
    else:
        while n % d != 0:
            r = n // d
            n -= r + 1
            d -= 1
            print(r + 1)
            
        for _ in range(d):
            print(r)
        

    return 0

if __name__ == "__main__":
    main()
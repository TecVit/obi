def main():
    n = int(input())
    o = str(input())
    h = str(input())

    c = 0

    for i in range(n):
        a, b = o[i], h[i]
        if a == b and a == "C":
            c += 1

    print(c)

if __name__ == "__main__":
    main()
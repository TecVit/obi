def main():
    n = int(input())
    p = [1]

    c = 0
    while p[c] < n:
        p.append(p[c] + (c + 2))
        c += 1

    if n in p:
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()
def main():
    n = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    lm = n // 2
    ch = (x1 <= lm and x2 > lm) or (x2 <= lm and x1 > lm)

    cm = n // 2
    cv = (y1 <= cm and y2 > cm) or (y2 <= cm and y1 > cm)

    if ch or cv:
        print("S")
    else:
        print("N")

    return 0;

if __name__ == "__main__":
    main()
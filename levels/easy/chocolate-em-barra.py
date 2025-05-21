def main():
    n = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    d = n // 2

    if abs(x1 - x2) >= d or abs(y1 - y2) >= d:
        print("S")
    else:
        print("N")

    return 0;

if __name__ == "__main__":
    main()
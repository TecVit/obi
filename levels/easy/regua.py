def main():
    n = int(input())
    x, y = map(int, input().split())

    r = abs(max(x, y) - min(x, y))

    if r >= n:
        print("EH SUFICIENTE")
    else:
        print("NAO EH SUFICIENTE")

if __name__ == "__main__":
    main()
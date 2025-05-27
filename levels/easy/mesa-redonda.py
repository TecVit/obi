def main():
    a = int(input())
    b = int(input())

    ca = 0
    for _ in range(a):
        ca = (ca + 1) % 3

    cb = 0
    for _ in range(b):
        cb = (cb + 1) % 3

    if cb == ca:
        cb = (cb + 1) % 3

    cc = 3 - ca - cb
    print(cc)

if __name__ == "__main__":
    main()
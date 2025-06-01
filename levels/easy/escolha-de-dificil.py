def main():
    ca, ba, pa = map(int, input().split())
    cr, br, pr = map(int, input().split())

    r = min(0, ca - cr) + min(0, ba - br) + min(0, pa - pr)

    print(abs(r))

    return 0

if __name__ == "__main__":
    main()
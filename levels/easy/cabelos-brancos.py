def main():
    e = float(input())
    g = float(input())

    if g * 0.73 >= e:
        print("ETANOL")
    else:
        print("GASOLINA")

    return 0

if __name__ == "__main__":
    main()
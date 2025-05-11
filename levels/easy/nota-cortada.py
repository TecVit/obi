def main():
    b = int(input())
    t = int(input())

    area_total = (70 * 160)
    area_cortada = area_total - (((b + t) * 70) / 2)

    if (area_total * 0.5 == area_cortada):
        print(0)
    elif (area_total * 0.5 > area_cortada):
        print(1)
    else:
        print(2)

if __name__ == "__main__":
    main()
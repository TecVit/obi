def numbersBinaryWithOne(n):
    SUM = 0
    for exponent in range(len(n)):
        SUM += (1 * (2 ** exponent))
    return SUM


def main():
    n = int(input())
    
    numbers = []

    for i in range(1, 100, 1):
        numbers.append([1] * i)

    response = list(numbersBinaryWithOne(number) for number in numbers)
    
    if n in response:
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()

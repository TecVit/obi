def decimalNumber(number):
    lenght = len(str(number))
    
    decimal = number - int(number)

    return decimal

def main():
    import math 
    x, y = map(int, input().split())
    n = x + y

    menor = min(x, y)
    maior = max(x, y)

    h = (x ** 2 + y ** 2) ** (1 / 2)
    c = (maior ** 2 - menor ** 2) ** (1 / 2)

    if decimalNumber(h) < decimalNumber(c):
        print(f"{h:.2f}")
    else:
        print(f"{c:.2f}")

    return 0

if __name__ == "__main__":
    main()
def main():
    from decimal import Decimal, getcontext, ROUND_DOWN

    getcontext().prec = 20

    N = int(input())

    for _ in range(N):
        A, B, C, D = map(int, input().split())
        delta_consumo = Decimal(D - B)
        delta_ano = Decimal(C - A)
        taxa = (delta_consumo / delta_ano).quantize(Decimal("0.01"), rounding=ROUND_DOWN)
        
        print(str(taxa).replace('.', ','))

if __name__ == "__main__":
    main()
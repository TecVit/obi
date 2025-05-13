def main():
    l = input()
    n = list(str(x) for x in l)
    nf = list(str(x) for x in l)

    for i in range(len(n)):
        if nf[i] == '6':
            nf[i] = '9'
        elif nf[i] == '9':
            nf[i] = '6'
        elif nf[i] == '8':
            nf[i] = '8'
        elif nf[i] == '0':
            nf[i] = '0'
        elif nf[i] == '1':
            nf[i] = '1'
        else:
            print("Nao")
            return 0

    for i in range(len(n)):
        if n[i] != nf[len(n) - 1 - i]:
            print("Nao")
            return 0
        
    print("Sim")

    return 0

if __name__ == "__main__":
    main()
def isPrime(number):
    if number < 2:
        return False
    
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
        
    return True

def main() -> int:
    n, x = map(int, input().split())
    ns = list()

    for i in range(n, x + 1):
        if not isPrime(i):
            ns.append(i)

    print(*ns)

    return 0

if __name__ == "__main__":
    main()
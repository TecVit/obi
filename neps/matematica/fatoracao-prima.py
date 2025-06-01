def primesOfNumber(number):
    primes = list()

    for n in range(2, number + 1):
        prime = True
        for j in range(2, int((number) ** (1 / 2)) + 1):
            if n % j == 0 and n != j:
                prime = False
                continue
        
        if prime:
            primes.append(n)

    return primes

def main():
    n = int(input())
    primes = list(int(x) for x in primesOfNumber(n) if x <= n)
    result = list()

    i = 0
    while n > 0 and i < len(primes):
        prime = primes[i]
        if n % prime == 0:
            n //= prime
            result.append(prime)
        else:
            i += 1

    print(len(result))
    print(*result)

    return 0

if __name__ == "__main__":
    main()
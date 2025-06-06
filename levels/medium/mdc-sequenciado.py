def primesOfN(n):
  primes = list()

  for i in range(2, int(n) + 1):
    prime = True
    for j in range(2, i + 1):
      if i % j == 0 and i != j:
        prime = False
        break
    
    if prime:
      primes.append(i)

  return primes

def main():
  n = int(input())
  ns = list(map(int, input().split()))
  primes = primesOfN(max(ns))
  print(primes)

  multiplication_primes = 1
  
  for prime in primes:
    dividido = [False for _ in range(n)]
    
    for i in range(n):
      if ns[i] % prime == 0:
        dividido[i] = True
        ns[i] /= prime

    if all(dividido):
      multiplication_primes *= prime
      
  print(multiplication_primes)

  return 0

if __name__ == "__main__":
  main()
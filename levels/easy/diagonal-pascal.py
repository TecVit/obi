MOD = 10**9 + 7

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % MOD
    return a


n = int(input())

print(fibonacci(n))
def main():
    N = int(input())
    digits = list(map(int, input().split()))

    def match(a):
        i = 0
        while i < N:
            num = a
            # calcular número de dígitos
            stack = []
            while num > 0:
                stack.append(num % 10)
                num //= 10
            if not stack:
                stack.append(0)
            for d in reversed(stack):
                if i >= N or digits[i] != d:
                    return False
                i += 1
            a += 1
        return True

    for a in range(1, 10**6):
        if match(a):
            print(a)
            return

if __name__ == "__main__":
  main()
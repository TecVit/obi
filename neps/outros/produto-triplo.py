n = int(input())
a = list(map(int, input().split()))

a.sort()

prod1 = a[-1] * a[-2] * a[-3]
prod2 = a[0] * a[1] * a[-1]

print(max(prod1, prod2))
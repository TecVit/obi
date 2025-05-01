# Não terminado

n, k = map(int, input().split())
p = [(int(h), i + 1) for i, h in enumerate(input().split())]
p.sort(reverse=True)

print(p)

c = n
s = 0
while c <= 0:

  for i in range(k):
    maior = p[i][0]
    if p[n-i-1][0] > maior:
      maior = p[n-i-1][0]

  s += maior * k
  c -= k

print(s)
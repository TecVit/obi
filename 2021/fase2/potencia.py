# Pontuação = 100 / 100
n = int(input())

res = 0
for i in range(n):
  t = str(input())
  e = t[-1]
  num = t[:-1]
  res += int(num) ** int(e)

print(res)
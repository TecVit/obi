# Pontuação = 100
def sumNumbers(number):
  sum = 0
  for i in number:
    sum += int(i)
  return sum

s = int(input())
a = int(input())
b = int(input())

res = 0
for num in range(a, b+1, 1):
  sum = sumNumbers(str(num))
  if sum == s:
    res += 1

print(res)
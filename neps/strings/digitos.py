length = int(input())
numbers = input().split()

maior = float("-inf")

l, r = 0, length - 1
while True:
  a = numbers[l]
  b = numbers[r]
  if a < b:
    if maior > a:
      maior = a
  l += 1
  
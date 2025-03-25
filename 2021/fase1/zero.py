# Pontuação = 100 / 100
quantidade = int(input())
numbers = []

for i in range(quantidade):
  number = int(input())
  if number == 0:
    numbers.pop()
  else:
    numbers.append(number)

print(sum(numbers))
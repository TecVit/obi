def verifyDigits(numbers):
  before = numbers[0]
  for number in numbers:
    if number != before:
      return False
  return True

def main():
  n = int(input())

  p = 'Nepo'
  c = 0

  for number in range(n, 0, -1):
    response = verifyDigits([int(b) for b in str(number)])
    
    if response:
      if n - number <= 0:
        # print(n - number)
        continue

      n -= number
      c += 1
      p = 'Muceno' if p == 'Nepo' else 'Nepo'

  print(p)

if __name__ == "__main__":
  main()
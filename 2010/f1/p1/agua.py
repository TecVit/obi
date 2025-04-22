def main():
  c = int(input())
  total = 7
      
  if c > 10:
    faixa_1 = min(c, 30) - 10
    total += faixa_1 * 1

  if c > 30:
    faixa_2 = min(c, 100) - 30
    total += faixa_2 * 2

  if c > 100:
    faixa_3 = c - 100
    total += faixa_3 * 5

  print(total)

if __name__ == "__main__":
  main()
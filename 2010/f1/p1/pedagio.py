def main():
  l, d = map(int, input().split())
  k, p = map(int, input().split())
  total = l * k
  qtd_p = 0

  while l >= d:
    l -= d
    qtd_p += 1

  total += qtd_p * p

  print(total)

if __name__ == "__main__":
  main()
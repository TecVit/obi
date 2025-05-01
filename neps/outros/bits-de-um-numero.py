def main():
  n = int(input())

  qtd = bin(n).count('1')
  print(qtd)

if __name__ == "__main__":
  main()
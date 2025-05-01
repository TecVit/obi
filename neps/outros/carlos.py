def main():
  filho = float("inf")
  pai = float("-inf")

  for i in range(10):
    idade = int(input())
    if idade > pai:
      pai = idade
    if idade < filho:
      filho = idade

  print(filho, pai)

if __name__ == "__main__":
  main()
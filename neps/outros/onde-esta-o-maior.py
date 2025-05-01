def main():
  maior = float("-inf")
  y, x = 0, 0
  for i in range(3):
    numeros = [int(x) for x in input().split()]
    for j in range(3):
      if numeros[j] > maior:
        maior = numeros[j]
        y, x = i, j
      
  print(f"Linha: {y}")
  print(f"Coluna: {x}")

if __name__ == "__main__":
  main()
def main():
  numero = int(input())
  divisores = []

  for divisor in range(numero, 0, -1):
    if (numero % divisor) == 0:
      divisores.append(divisor)
  
  divisores.sort()

  print(f"{len(divisores)} divisor(es):", end=" ")
  
  for divisor in divisores:
    print(divisor, end=" ")
  print()
  
  print(f"Soma de divisores = {sum(divisores)}")

  print(f"{"Primo" if len(divisores) == 2 else "Nao primo"}")

if __name__ == "__main__":
  main()
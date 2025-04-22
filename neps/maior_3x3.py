def main():
  matriz = []
  row = []
  
  maior = float("-inf")
  for i in range(9):
    n = int(input())
    if n > maior:
      maior = n
    row.append(n)
    if (i+1) % 3 == 0:
      matriz.append(row)
      row = []

  for i in range(3):
    for j in range(3):
      if matriz[i][j] == maior:
        print(-1, end=" ")
      else:
        print(matriz[i][j], end=" ")
    print()

if __name__ == "__main__":
  main()
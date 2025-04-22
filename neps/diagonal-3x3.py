def main():
  matriz = []
  row = []
  
  for i in range(9):
    n = int(input())
    row.append(n)
    if (i+1) % 3 == 0:
      matriz.append(row)
      row = []

  sum_diag1 = 0
  sum_diag2 = 0
  for i in range(3):
    sum_diag1 += matriz[i][i]
    sum_diag2 += matriz[i][(3-1) - i]

  print(f"Diagonal principal: {sum_diag1}")
  print(f"Diagonal secundaria: {sum_diag2}")

if __name__ == "__main__":
  main()
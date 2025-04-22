def main():
  matriz = []
  row = []
  
  for i in range(9):
    n = int(input())
    row.append(n)
    if (i+1) % 3 == 0:
      matriz.append(row)
      row = []

  sum_row = 0
  sum_column = 0
  for i in range(3):
    r = sum(matriz[i])
    c = 0
    for j in range(3):
      c += matriz[j][i]
    
    if i != 0:
      if r != sum_row or c != sum_column:
        print("NAO")
        return
    else:
      sum_row = r
      sum_column = c

  sum_diag1 = 0
  sum_diag2 = 0
  for i in range(3):
    sum_diag1 += matriz[i][i]
    sum_diag2 += matriz[i][(3-1) - i]

  if sum_diag1 != sum_diag2:
    print('NAO')
  else:
    print("SIM")

if __name__ == "__main__":
  main()
def main():
  n, m = map(int, input().split())
  pinos = list(map(int, input().split()))
  movimentos = 0

  for i in range(n - 1):
    diff = m - pinos[i]
    pinos[i] += diff
    pinos[i + 1] += diff
    movimentos += abs(diff)
  
  print(movimentos)

if __name__ == "__main__":
  main()
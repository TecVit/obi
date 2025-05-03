def main():
  ns = [int(input()) for x in range(10)]
  m = min(x for x in ns)
  ni = []
  
  for i in range(10):
    n = ns[i]
    if n == m:
      ni.append(i)
      ns[i] = -1

  print(f"Menor: {m}")
  print(f"Ocorrencias: ", end="")
  print(*ni)
  print(*ns)
  
if __name__ == "__main__":
  main()
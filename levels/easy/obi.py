def main():
  n, p = map(int, input().split())
  s = 0
  for i in range(n):
    a, b = map(int, input().split())
    if a + b >= p:
      s += 1
  
  print(s)
  return 0

if __name__ == "__main__":
  main()
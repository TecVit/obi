def main():
  n = int(input())
  ns = list(map(int, input().split()))
  r = list(0 for _ in range(n))

  for i in range(n):
    r[i] = ns.count(i)
    
  print(*r)
  
if __name__ == "__main__":
  main()
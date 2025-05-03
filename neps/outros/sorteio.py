def main():
  n = int(input())
  ns = list(map(int, input().split()))

  print(ns[0])

  if n % 2 == 0:
    print(ns[int(((n / 2) - 1))])
  else:
    print(ns[int((n - 1) / 2)])

  print(ns[n-1])
  
if __name__ == "__main__":
  main()
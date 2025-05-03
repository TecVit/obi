def main():
  n, m = map(int, input().split())
  a = list(map(int, input().split()))

  b = [0] * n

  for i in a:
    b[i - 1] += 1

  print(max(b))

  
if __name__ == "__main__":
  main()
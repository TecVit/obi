def main():
  n, c = map(int, input().split())
  s = 0

  for i in range(n):
    s += max(1, c - i)

  print(s)

if __name__ == "__main__":
  main()
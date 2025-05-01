def main():
  n = int(input())
  s = 0

  for i in range(n, 0, -1):
    s += i

  print(s)

if __name__ == "__main__":
  main()
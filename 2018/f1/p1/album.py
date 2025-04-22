def main():
  n = int(input())
  m = int(input())
  a = set()

  for i in range(m):
    b = int(input())
    a.add(b)

  print(n - len(a))

if __name__ == "__main__":
  main()
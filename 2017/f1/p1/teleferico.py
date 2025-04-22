def ceil(x):
  return int(x) if x == int(x) else int(x) + 1

def main():
  c = int(input())
  a = int(input())

  print(ceil(a / (c - 1)))

if __name__ == "__main__":
  main()
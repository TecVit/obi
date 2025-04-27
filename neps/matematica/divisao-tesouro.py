from math import ceil

def main():
  c = int(input())
  p = int(input())

  a = ceil(c / (p + 2))
  r = a * 2

  print(r)

if __name__ == "__main__":
  main()
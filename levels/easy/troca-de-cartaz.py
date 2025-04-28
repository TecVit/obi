def main():
  na, nb = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  x = set(a)
  y = set(b)

  xy = x - y
  yx = y - x

  result = min(len(xy), len(yx))

  print(result)
  return 0

if __name__ == "__main__":
  main()
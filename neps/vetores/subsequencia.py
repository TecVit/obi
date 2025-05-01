def main():
  a, b = map(int, input().split())
  xs = list(map(int, input().split()))
  ys = list(map(int, input().split()))

  j = 0

  for i in range(b):
    while j < a and xs[j] != ys[i]:
      j += 1
    if j == a:
      print("N")
      return
    j += 1

  print("S")
  return 0

if __name__ == "__main__":
  main()  
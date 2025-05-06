def main():
  x0, y0, x1, y1 = map(int, input().strip().split())
  a0, b0, a1, b1 = map(int, input().strip().split())

  if not (x1 < a0 or a1 < x0 or y1 < b0 or b1 < y0):
    print(1)
  else:
    print(0)

if __name__ == "__main__":
  main()
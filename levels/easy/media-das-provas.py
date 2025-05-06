def main():
  a, pa = map(int, input().split())
  b, pb = map(int, input().split())
  c, pc = map(int, input().split())

  r = ((a * pa) + (b * pb) + (c * pc)) / (pa + pb + pc)

  print(int(r))

if __name__ == "__main__":
  main()
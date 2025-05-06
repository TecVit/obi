def main():
  a, b, c, d = map(int, input().split())
  ps = list()

  ps.append((a+b) - (c+d))
  ps.append((a+c) - (b+d))
  ps.append((a+d) - (c+b))
  ps.append((c+d) - (a+b))
  ps.append((b+d) - (a+c))
  ps.append((c+b) - (a+d))

  ps = [p for p in ps if p >= 0]
  
  print(min(ps))

if __name__ == "__main__":
  main()
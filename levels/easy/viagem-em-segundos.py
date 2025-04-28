def main():
  d1 = int(input())
  h1 = int(input())
  m1 = int(input())

  d2 = int(input())
  h2 = int(input())
  m2 = int(input())

  ds = (d2 * 86400) - (d1 * 86400)
  hs = (h2 * 3600) - (h1 * 3600)
  ms = (m2 * 60) - (m1 * 60)

  print(ds + hs + ms)

if __name__ == "__main__":
  main()
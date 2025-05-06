def main():
  p = str(input()).split()

  for i in range(len(p)):
    l = p[i]
    p[i] = l.swapcase()

  print(*p)

if __name__ == "__main__":
  main()
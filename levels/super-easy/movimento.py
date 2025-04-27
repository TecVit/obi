def main():
  a, b, c = int(input()), int(input()), int(input())
  s = a + b
  c += 0.5

  if s <= c:
    print(1)
  else:
    print(0)

if __name__ == "__main__":
  main()
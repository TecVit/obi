def main():
  n = int(input())
  t = (n / 8)

  if t > n // 8:
    print((n // 8) + 1)
  else:
    print(int(t))

if __name__ == "__main__":
  main()
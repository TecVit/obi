def main():
  N = int(input())

  for i in range(2, int(N ** 0.5) + 1):
    if N % i == 0:
      if N // i > 1:
        print("S")
        return
  print("N")

if __name__ == "__main__":
  main()
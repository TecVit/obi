def main():
  n = int(input())
  print(int(bin(n - 1)[2:], 3))

if __name__ == "__main__":
  main()
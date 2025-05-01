def main():
  n = int(input())
  v = list(map(int, input().split()))

  print(f"{sum(v) / n:.2f}")

if __name__ == "__main__":
  main()
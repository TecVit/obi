def main():
  a, b, c, d = map(int, input().split())
  d = ( ((a - c) ** 2) + ((b - d) ** 2) ) ** ( 1 / 2 )
  
  print(f"{d:.2f}")

if __name__ == "__main__":
  main()
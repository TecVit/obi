def main():
  a, b, x, y = map(int, input().split())

  print(abs(x - a) + abs(y - b))

if __name__ == "__main__":
  main()
def main():
  n = int(input())

  for i in range(n):
    a, b = map(str, input().split())
    a = int(a)
    print(a * b)

if __name__ == "__main__":
  main()
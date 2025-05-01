def main():
  n = int(input())

  for i in range(n):
    a, b = map(str, input().split(" ", 1))
    a = int(a)

    a = a % len(b)
    b = b[a:] + b[:a]

    print(b)
    
  return 0

if __name__ == "__main__":
  main()
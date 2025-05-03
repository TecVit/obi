def sortOdd(n, v):
  s = v
  s.sort()

  s = [x for x in s if x % 2 != 0]
  
  return s

def main():
  n = int(input())
  v = list(map(int, input().split()))

  a = [x for x in v if x % 2 == 0]
  s = sortOdd(n, v)
  r = s + a

  print(*r)

if __name__ == "__main__":
  main()
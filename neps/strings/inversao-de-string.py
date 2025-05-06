def main():
  n, a, b = map(int, input().split())
  s = list(str(x) for x in input())

  l = s[a-1:b]
  for i in range(len(l)):
    x = l[len(l)-1-i]
    s[i+a-1] = x

  for x in s:
    print(x, end="")

if __name__ == "__main__":
  main()
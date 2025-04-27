def main():
  n = int(input())
  
  l = float("-inf")
  s = float("inf")
  for i in range(n):
    a = int(input())
    if a > l:
      l = a
    if a < s:
      s = a

  print(l)
  print(s)

if __name__ == "__main__":
  main()
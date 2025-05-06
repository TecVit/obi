def main():
  n = int(input())
  p = list(str(x) for x in input())

  for i in range(n - 2):
    l = p[i] + p[i+1] + p[i+2]
    if l == 'joi':
      l = l.upper()
      p[i], p[i+1], p[i+2] = l[0], l[1], l[2]
  
  for l in p:
    print(l, end="")

if __name__ == "__main__":
  main()
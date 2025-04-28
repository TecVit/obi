def main():
  n = int(input())
  rs = {}
  l = []

  for i in range(n):
    j = int(input())
    if j in rs:
      rs[j] += 1
    else:
      rs[j] = 1

  for key in rs.keys():
    qtd = rs[key]
    num = key
    l.append((qtd, num))
  
  l.sort()
  g = l[len(l) - 1][0]

  for a, b in l:
    if a == g:
      print(b, end=" ")

if __name__ == "__main__":
  main()
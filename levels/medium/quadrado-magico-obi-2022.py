# 50 / 100 

def main():
  n = int(input())
  m = []
  l = []

  x, y = 0, 0

  for i in range(n):
    row = [int(x) for x in input().split()]
    if 0 in row:
      x = row.index(0) + 1
    l.append((sum(row), i))
    m.append(row)

  l.sort()
  y = l[0][1] + 1

  t = max(sum(m[0]), sum(m[1]), sum(m[2])) - min(sum(m[0]), sum(m[1]), sum(m[2]))

  print(t)
  print(y)
  print(x)

if __name__ == "__main__":
  main()
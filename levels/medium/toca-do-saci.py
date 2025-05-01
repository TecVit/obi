def main():
  a, b = map(int, input().split())
  m = [[0 for _ in range(b + 2)]]
  
  y, x = 0, 0
  ya, xa = 0, 0
  
  for i in range(a):
    row = [0] + [int(x) for x in input().split()] + [0]
    if 3 in row:
      y, x = i + 1, row.index(3)
    if 2 in row:
      ya, xa = i + 1, row.index(2)
    m.append(row)
  
  m.append([0 for _ in range(b + 2)])

  s = 1
  while y != ya or x != xa:
    m[y][x] = 0
    
    if m[y+1][x] >= 1:
      y += 1
    elif m[y-1][x] >= 1:
      y -= 1
    elif m[y][x+1] >= 1:
      x += 1
    elif m[y][x-1] >= 1:
      x -= 1

    s += 1

  print(s)
  return 0

if __name__ == "__main__":
  main()
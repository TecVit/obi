def main():
  a, b = map(int, input().split())
  m = [[0 for _ in range(b + 2)]]

  for i in range(a):
    row = [0] + [int(x) for x in input().split()] + [0]
    m.append(row)

  m.append([0 for _ in range(b + 2)])

  for i in range(1, a + 1):
    for j in range(1, b + 1):
      if m[i][j] == 0:
        continue

      c = 0

      if m[i-1][j] > 0:
        c += 1
      if m[i+1][j] > 0:
        c += 1
      if m[i][j+1] > 0:
        c += 1
      if m[i][j-1] > 0:
        c += 1

      m[i][j] = c

  for i in range(1, a + 1):
    row = m[i]
    for j in range(1, b + 1):
      print(row[j], end=" ")
    print()

if __name__ == "__main__":
  main()
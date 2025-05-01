def main():
  steps = input()
  m = [
    [1, 2],
    [3, 4]
  ];

  for step in steps:
    if step == "H":
      m[0][0], m[1][0] = m[1][0], m[0][0]
      m[0][1], m[1][1] = m[1][1], m[0][1]
    elif step == "V":
      m[0][0], m[0][1] = m[0][1], m[0][0]
      m[1][0], m[1][1] = m[1][1], m[1][0]

  for row in m:
    print(*row)

if __name__ == "__main__":
  main()
def main():
  o1, p1, b1 = map(int, input().split())
  o2, p2, b2 = map(int, input().split())

  media1 = ((o1 * 3) + (p1 * 2) + (b1 * 1)) / 6
  media2 = ((o2 * 3) + (p2 * 2) + (b2 * 1)) / 6

  if media1 > media2:
    print("A")
  elif media2 > media1:
    print("B")

  return 0

if __name__ == "__main__":
  main()
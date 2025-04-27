def main():
  s = input()
  t = len(s) - 2

  print(f"{s[0]}{t}{s[t+1]}")

if __name__ == "__main__":
  main()
def main():
  a = int(input())
  d = int(input())

  i = max(1, a - d)
  
  print(i)
  if i >= 18:
    print("Maior")
  else:
    print("Menor")

if __name__ == "__main__":
  main()
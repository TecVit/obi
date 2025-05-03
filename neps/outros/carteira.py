def main():
  a = int(input())
  d = int(input())

  i = max(1, a - d)
  
  print(i)
  
  if i >= 18:
    print("Pode tirar carteira")
  else:
    print("Nao pode tirar carteira")

  print(abs(i - 18))

if __name__ == "__main__":
  main()
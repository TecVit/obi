def main():
  a = int(input())
  d = int(input())

  i = max(1, a - d)
  
  print(i)
  
  if i >= 18 and i <= 67:
    print("Pode doar sangue")
  else:
    print("Nao pode doar sangue")

if __name__ == "__main__":
  main()
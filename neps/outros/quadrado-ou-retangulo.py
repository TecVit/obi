def main():
  a = int(input())
  b = int(input())

  if a == b:
    print(a*4)
    print("Quadrado")
  else:
    print(a*2 + b*2)
    print("Retangulo")

if __name__ == "__main__":
  main()
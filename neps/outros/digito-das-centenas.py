def main():
  n = int(input())
  
  if n <= 999 and n >= 100:
    c = n // 100
    print(c)
    if c % 2 == 0:
      print("Par")
    else:
      print("Impar")
  else:
    print("Valor invalido")

if __name__ == "__main__":
  main()
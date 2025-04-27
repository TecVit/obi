def main():
  palavra = input()
  t = len(palavra)

  for i in range(t):
    l1 = palavra[i]
    l2 = palavra[t-i-1]
    if l1 != l2:
      print("nao eh palindromo")
      return
    
  print("eh palindromo")

if __name__ == "__main__":
  main()
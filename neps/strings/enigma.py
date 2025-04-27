def main():
  cifras = str(input())
  palavra = str(input())

  c = 0
  for i in range(len(cifras) - len(palavra) + 1):
    for j in range(len(palavra)):
      letra_palavra = palavra[j]
      cifra = cifras[j+i]
      if letra_palavra == cifra:
        c -= 1
        break
    c += 1

  print(c)

if __name__ == "__main__":
  main()
def main():
  palavras = input().split()
  resposta = ''

  for palavra in palavras:
    for i in range(len(palavra)):
      if i % 2 != 0:
        resposta += palavra[i]

    resposta += ' '

  print(resposta)

if __name__ == "__main__":
  main()
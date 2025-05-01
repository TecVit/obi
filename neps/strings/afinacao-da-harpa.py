def main():
  instrucao = input().strip()

  letras = ''
  c = 0
  
  while c < len(instrucao):
    if instrucao[c] in '+-':
      sinal = instrucao[c]
      c += 1
      numero = ''

      while c < len(instrucao) and instrucao[c].isdigit():
        numero += instrucao[c]
        c += 1

      acao = "tighten" if sinal == '+' else "loosen"
      print(f"{letras} {acao} {int(numero)}")
      letras = ''
    else:
      letras += instrucao[c]
      c += 1

if __name__ == "__main__":
  main()
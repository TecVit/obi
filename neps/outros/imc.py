def main():
  idade = int(input())
  peso = float(input())
  altura = float(input())

  imc = peso / (altura ** 2)

  if imc >= 40:
    print('obesidade grau 3')
  elif imc >= 35:
    print('obesidade grau 2')
  elif imc >= 30:
    print('obesidade grau 2')
  elif imc >= 25:
    print('sobrepeso')
  elif imc >= 18:
    print('peso adequado')
  else:
    print('baixo peso')

if __name__ == "__main__":
  main()
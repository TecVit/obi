def main():
  pessoas = int(input())
  maior = float('-inf')
  idade_maior = maior

  for i in range(pessoas):
    idade, peso, altura = map(float, input().split())
    imc = peso / (altura ** 2)
    if imc > maior:
      maior = imc
      idade_maior = idade

  print(f"A pessoa com o maior IMC tem {int(idade_maior)} anos.")

if __name__ == "__main__":
  main()
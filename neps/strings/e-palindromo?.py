def main():
  numero = input()
  binario = bin(int(numero))[2:]

  t_numero = len(numero)
  t_binario = len(binario)

  for i in range(t_binario):
    l1 = binario[i]
    l2 = binario[t_binario-i-1]
    if l1 != l2:
      print("N")
      return
    
  for i in range(t_numero):
    l1 = numero[i]
    l2 = numero[t_numero-i-1]
    if l1 != l2:
      print("N")
      return
    
  print("S")

if __name__ == "__main__":
  main()
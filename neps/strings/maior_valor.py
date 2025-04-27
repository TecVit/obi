def main():
  a = int(input())
  b = int(input())
  t = int(input())

  maior = float("-inf")
  for i in range(a, b + 1): # Se der errado, utilizar b + 1
    soma = sum([int(x) for x in str(i)])
    if soma == t:
      if i > maior:
        maior = i

  print(max(-1, maior))

if __name__ == "__main__":
  main()
def main():
  a = int(input())
  b = int(input())
  c = int(input())

  respostas = [
    (b * 2) + (c * 4),
    (a * 2) + (c * 2),
    (a * 4) + (b * 2)
  ]
  
  respostas.sort()

  print(respostas[0])

if __name__ == "__main__":
  main()
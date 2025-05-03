def main():
  n = int(input())
  for _ in range(n):
    palavra = input()
    resultado = []

    c = 1
    for i in range(1, len(palavra) + 1):
      if i < len(palavra) and palavra[i] == palavra[i - 1]:
          c += 1
      else:
          resultado.append((c, palavra[i - 1]))
          c = 1

    for count, letra in resultado:
        print(f"{count} {letra}", end=" ")
    print()

if __name__ == "__main__":
  main()
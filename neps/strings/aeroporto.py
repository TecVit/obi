def main():
  teste = 1
  while True:
    linha = input()
    A, V = map(int, linha.split())

    if A == 0 and V == 0:
      break

    trafego = [0] * (A + 1)

    for _ in range(V):
      X, Y = map(int, input().split())
      trafego[X] += 1
      trafego[Y] += 1

    max_trafego = max(trafego[1:])
    aeroportos_congestionados = [
        str(i) for i in range(1, A + 1) if trafego[i] == max_trafego
    ]

    print(f"Teste {teste}")
    print(" ".join(aeroportos_congestionados))
    print()

    teste += 1

if __name__ == "__main__":
  main()
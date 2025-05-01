import bisect

def main():
  qtd_faixas, qtd_ogros = map(int, input().split())
  faixas_premiacoes = list(map(int, input().split()))
  premiacoes = list(map(int, input().split()))
  ogros = list(map(int, input().split()))
  resultados = []

  # aplicando busca binaria :)
  for ogro in ogros:
    idx = bisect.bisect_right(faixas_premiacoes, ogro)
    resultados.append(premiacoes[idx])

  print(*resultados)

if __name__ == "__main__":
  main()
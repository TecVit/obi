def main():
  n = int(input())
  c = []
  p = []

  for i in range(n):
    nome, valor = map(str, input().split())
    c.append((int(valor), i))
    p.append(nome)

  c.sort(reverse=True)

  for i in range(n - 1):
    pessoa, valor = p[c[i][1]], c[i][0]
    fut_pessoa, fut_valor = p[c[i+1][1]], c[i+1][0]
    if valor == fut_valor:
      a = [pessoa, fut_pessoa]
      a.sort()

      p[c[i][1]], p[c[i+1][1]] = a[0], a[1]

  for i in range(n):
    print(p[c[i][1]])

if __name__ == "__main__":
  main()
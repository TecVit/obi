def main():
  n = int(input())
  ps = []

  for _ in range(n):
    a = float(input())
    ps.append(a)

  for p in ps:
    if p <= 1.55:
      print('Aceito')
    else:
      print('Nao aceito')

if __name__ == "__main__":
  main()
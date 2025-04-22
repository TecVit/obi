def main():
  n, m = map(int, input().split())
  cofre = [0] + [int(x) for x in input().split()]
  etapas = [int(x) for x in input().split()]
  resultado = [0 for _ in range(10)]

  end = float("inf")
  for i in range(m - 1):
    l = min(etapas[i], etapas[i+1])
    r = max(etapas[i], etapas[i+1])
    
    a, b = 0, 0
    
    if r == end:
      b += 1
    elif l == end:
      a += 1

    end = etapas[i+1]
    f = cofre[l+a:r+1-b]

    v = []
    for num in f:
      if not num in v:
        resultado[num] += f.count(num)
        v.append(num)

  for n in resultado:
    print(n, end=" ")

if __name__ == "__main__":
  main()
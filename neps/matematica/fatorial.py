def menor_quantidade_fatoriais(N):
  fatoriais = []

  f = 1
  i = 1

  while f <= N:
    fatoriais.append(f)
    i += 1
    f *= i
  
  count = 0
  idx = len(fatoriais) - 1
  
  while N > 0:
    if fatoriais[idx] <= N:
      N -= fatoriais[idx]
      count += 1
    else:
      idx -= 1

  return count

n = int(input())
print(menor_quantidade_fatoriais(n))
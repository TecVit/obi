# 22 / 100

def eh_anti_progressao(seq, novo):
  for i in range(len(seq)):
    for j in range(i + 1, len(seq)):
      if seq[i] + novo == 2 * seq[j]:
        return False
      if seq[j] + novo == 2 * seq[i]:
        return False
      if seq[i] + seq[j] == 2 * novo:
        return False
  return True


def anti_progressao_n_esimo(N):
  seq = [0]
  usados = set(seq)
  x = 1

  while len(seq) < N:
    eh_valido = True
    for a in seq:
      b = (x + a) // 2
      if (x + a) % 2 == 0 and b in usados:
        eh_valido = False
        break
    if eh_valido:
      seq.append(x)
      usados.add(x)
    x += 1

  return seq[-1]

n = int(input())
print(anti_progressao_n_esimo(n))
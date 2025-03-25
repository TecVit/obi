# Pontuação = 100 / 100
def encontrar_menor_c(a, b):
  c = 2 * a - b
  return c

a, b = map(int, input().split())
print(encontrar_menor_c(a, b))
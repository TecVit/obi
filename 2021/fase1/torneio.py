# Pontuação = 100
vitorias = 0

for i in range(6):
  resultado = str(input())
  if resultado == "V":
    vitorias += 1

if vitorias >= 5:
  print(1)
elif vitorias >= 3:
  print(2)
elif vitorias >= 1:
  print(3)
else:
  print(-1)
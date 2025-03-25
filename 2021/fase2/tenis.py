# Pontuação = 100 / 100
js = []
for i in range(4):
  j = int(input())
  js.append(j)

js.sort()
print( abs((js[0] + js[-1]) - (js[1] + js[-2])) )
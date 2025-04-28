# Grandes Prêmios e Números de Pilotos
g, p = map(int, input().split())

pilotos = [0 for _ in range(p)]

# Resultado de uma corrida
for i in range(g):
  # Corrida
  posicoes = [int(x) for x in input().split()]
  pilotos[i] = posicoes[i] # O i-ésimo número indica a ordem de chegada do piloto i na corrida 

# Número de sistemas de pontuação
s = int(input())

# Sistemas de pontuações
for i in range(s):
  ps = [int(x) for x in input().split()]
  mn_p, ps = ps[0], ps[1:]
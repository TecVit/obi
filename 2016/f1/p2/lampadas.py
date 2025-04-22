def interruptorA(luz):
  if luz == 0:
    luz = 1
  else:
    luz = 0
    
  return luz

def interruptorB(luzes):
  if luzes[0] == 0:
    luzes[0] = 1
  else:
    luzes[0] = 0

  if luzes[1] == 0:
    luzes[1] = 1
  else:
    luzes[1] = 0

  return luzes

def main():
  fases = [int(x) for x in input().split()]

  lampadaA = fases[0]
  lampadaB = fases[1]

  metaA = fases[2]
  metaB = fases[3]

  p = 0

  if metaB != lampadaB:
    luzes = interruptorB([lampadaA, lampadaB])
    lampadaA, lampadaB = luzes[0], luzes[1]
    p += 1

  if metaA != lampadaA:
    luz = interruptorA(lampadaA)
    lampadaA = luz
    p += 1

  print(p)

if __name__ == "__main__":
  main()
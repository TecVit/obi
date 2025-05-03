def main():
  cidades = list(map(int, input().split()))
  
  pos = [0]
  for d in cidades:
    pos.append(pos[-1] + d)

  for i in range(5):
    linha = []
    for j in range(5):
      linha.append(abs(pos[i] - pos[j]))
    print(*linha)

if __name__ == "__main__":
  main()
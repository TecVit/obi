def main():
  n = int(input())
  v = list(map(int, input().split()))

  m = int(input())
  
  for i in range(m):
    x = [int(x) for x in input().split()]
    if x[0] == 1:
      v.pop()
    elif x[0] == 2:
      v.append(x[1])
  
  if len(v) > 0:
    print(*v)
  else:
    print("Pilha vazia")

if __name__ == "__main__":
  main()
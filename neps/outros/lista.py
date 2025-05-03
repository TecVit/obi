def main():
  n = int(input())
  v = list(map(int, input().split()))

  m = int(input())
  
  for i in range(m):
    x = [int(x) for x in input().split()]
    if x[0] == 1:
      v.remove(x[1])
    elif x[0] == 2:
      v = [v[i] for i in range(len(v)) if i != x[1]]
    elif x[0] == 3:
      v = [x[1]] + v
    elif x[0] == 4:
      v.append(x[1])
  
  if len(v) > 0:
    print(*v)
  else:
    print("Lista vazia.")

if __name__ == "__main__":
  main()
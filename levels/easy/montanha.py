def main():
  lenght = int(input())
  numbers = [int(x) for x in input().split()]

  s = 0
  for i in range(1, lenght - 1):
    a, b, c = numbers[i-1], numbers[i], numbers[i+1]
    if a > b and c > b:
      s += 1
    
  if s >= 1:
    print('S')
  else:
    print('N')

if __name__ == "__main__":
  main()
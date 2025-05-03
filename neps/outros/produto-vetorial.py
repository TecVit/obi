def main():
  x1, y1, x2, y2 = map(int, input().split())
  prod = (x1 * y2) - (x2 * y2)

  if prod == 0:
    print("Produto vetorial paralelo")
  elif prod > 0:
    print("Angulo maior que 180 graus")
  else:
    print("Angulo menor que 180 graus")
  
if __name__ == "__main__":
  main()
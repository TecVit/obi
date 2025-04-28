def main():
  a, b = map(int, input().split())
  c, d = map(int, input().split())

  print("Primeiro" if a * b > c * d else "Segundo" if a * b < c * d else "Empate" )

if __name__ == "__main__":
  main()
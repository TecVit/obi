def main():
  ha = int(input())
  ma = int(input())
  hr = int(input())
  mr = int(input())

  a = (ha * 60) + ma + 45
  r = (hr * 60) + mr

  p = a - r
  if p <= 0:
    print("Sucesso")
  else:
    print(f"Atrasado {abs(p)}")

if __name__ == "__main__":
  main()
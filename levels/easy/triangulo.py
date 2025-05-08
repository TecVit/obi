def main():
  a, b, c, d = map(int, input().split())

  def forma_triangulo(x, y, z):
    return x < y + z and y < x + z and z < x + y

  if (forma_triangulo(a, b, c) or
    forma_triangulo(a, b, d) or
    forma_triangulo(a, c, d) or
    forma_triangulo(b, c, d)):
    print('S')
  else:
    print('N')

if __name__ == "__main__":
  main()
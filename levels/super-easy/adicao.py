def main():
  a, b, c = map(int, input().split())

  print("wrong!" if a + b != c else "correct!")
  
if __name__ == "__main__":
  main()
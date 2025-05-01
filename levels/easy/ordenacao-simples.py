def main():
  numbers = [int(input()) for _ in range(10)]

  numbers.sort()
  for number in numbers:
    print(number, end=" ")
  print()
  
  numbers.sort(reverse=True)
  for number in numbers:
    print(number, end=" ")
  
if __name__ == "__main__":
  main()
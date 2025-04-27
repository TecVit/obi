import sys

def main():
  sys.set_int_max_str_digits(100010)
  n = int(input())

  print('S' if n % 2 == 0 else 'N')
  print('S' if n % 3 == 0 else 'N')
  print('S' if n % 5 == 0 else 'N')

if __name__ == "__main__":
  main()
def main():
  states = ["roraima", "acre", "amapa", "amazonas", "para", "rondonia", "tocantins"]
  state = input()

  if state in states:
    print('Regiao Norte')
  else:
    print('Outra regiao')

if __name__ == "__main__":
  main()
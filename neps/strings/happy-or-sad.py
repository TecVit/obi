def main():
  frase = input()
  happy = frase.count(":-)")
  sad = frase.count(":-(")

  if happy == 0 and sad == happy:
    print("none")
  elif happy > sad:
    print("happy")
  elif sad > happy:
    print("sad")
  elif sad == happy:
    print("unsure")
  
if __name__ == "__main__":
  main()
def main():
  frase = input().split()
  if frase[len(frase)-1] == "eh?":
    print("Canadian!")
  else:
    print("Imposter!")

if __name__ == "__main__":
  main()
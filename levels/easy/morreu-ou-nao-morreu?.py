def main():
    nome = str(input())
    ataque = int(input())
    defesa = int(input())
    vida = int(input())
    dano = int(input())

    final = vida - (dano - defesa)

    if final > 0:
        print(f"{nome} sobreviveu!!!")
    else:
        print(f"{nome} morreu :(")
          
if __name__ == "__main__":
    main()
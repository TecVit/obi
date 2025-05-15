T = int(input())
for _ in range(T):
    Q, Lq, Lr, Lp = map(int, input().split())
    total_linhas = Q * (Lq + Lr)
    paginas = (total_linhas + Lp - 1) // Lp
    if paginas == 1:
        print("O livro contera 1 pagina.")
    else:
        print(f"O livro contera {paginas} paginas.")
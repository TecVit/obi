def min_operacoes_para_palindromo(lista):
    i = 0
    j = len(lista) - 1
    operacoes = 0

    while i < j:
      if lista[i] == lista[j]:
        i += 1
        j -= 1
      elif lista[i] < lista[j]:
        lista[i+1] += lista[i]
        i += 1
        operacoes += 1
      else:
        lista[j-1] += lista[j]
        j -= 1
        operacoes += 1

    return operacoes

n = int(input())
lista = list(map(int, input().split()))

print(min_operacoes_para_palindromo(lista))
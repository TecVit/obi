def solve(idx=0, prod=1, qtd=0):
  if idx == k:
    ret = n // prod
    if qtd % 2 == 1:
      ret = -ret
    return ret

  ret = solve(idx + 1, prod, qtd)

  if prod * prime[idx] <= n:
    ret += solve(idx + 1, prod * prime[idx], qtd + 1)

  return ret


n, k = map(int, input().split())
prime = list(map(int, input().split()))

print(solve())
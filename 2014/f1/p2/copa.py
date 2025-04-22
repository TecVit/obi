# Copa do Mundo (OBI 2014)
def find(u, parent):
  if parent[u] != u:
    parent[u] = find(parent[u], parent)
  return parent[u]

def union(u, v, parent, size):
  u_root = find(u, parent)
  v_root = find(v, parent)

  if u_root == v_root:
    return False
  
  # Garantimos que (v_root) sempre sera o menor como variavel
  if size[u_root] < size[v_root]:
    u_root, v_root = v_root, u_root

  # Sempre o menor vai para o maior
  parent[v_root] = u_root
  size[u_root] += size[v_root]

  return True

def main():
  n, f, r = map(int, input().split())
  arestas = []

  # Ferrovias (tipo 1)
  for _ in range(f):
    a, b, c = map(int, input().split())
    arestas.append((1, c, a, b))  # (tipo, peso, u, v)

  # Rodovias (tipo 2)
  for _ in range(r):
    a, b, c = map(int, input().split())
    arestas.append((2, c, a, b))

  # Ordena primeiro por tipo (ferrovia primeiro), depois por peso crescente
  arestas.sort()

  parent = [i for i in range(n + 1)]
  size = [1] * (n + 1)

  custo_total = 0

  for tipo, peso, u, v in arestas:
    if union(u, v, parent, size):
      custo_total += peso

  print(custo_total)

if __name__ == "__main__":
  main()
def main():
  n = int(input())
  v = list(map(int, input().split()))
  s = int(input())

  if s in v:
    print("pertence")
  else:
    print("nao_pertence")

if __name__ == "__main__":
  main()
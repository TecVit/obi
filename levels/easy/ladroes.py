def main():
    n, m = map(int, input().split())
    
    t = (m * (n + 1))
    
    # Lógica
    # for i in range(n):
    #     t = (m * (2 + i))

    print(t)
    return 0

if __name__ == "__main__":
    main()
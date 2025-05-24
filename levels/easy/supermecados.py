def main():
    n = int(input())
    ps = list()

    for i in range(n):
        p, g = map(float, input().split())
        ps.append(round((p * (1000 / g)), 2))
    
    print(f"{min(ps):.2f}")

    return 0

if __name__ == "__main__":
    main()
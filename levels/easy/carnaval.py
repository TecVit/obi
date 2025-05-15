def main():
    ns = list(map(float, input().split()))
    ns.sort()

    print(f"{sum(ns[1:-1]):.1f}")
    return 0

if __name__ == "__main__":
    main()
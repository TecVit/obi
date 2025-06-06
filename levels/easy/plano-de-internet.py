def main():
    quota = int(input())
    n = int(input())
    
    r = quota

    for _ in range(n):
        mega = int(input())
        quota += (r - mega)

    print(quota)

    return 0

if __name__ == "__main__":
    main()
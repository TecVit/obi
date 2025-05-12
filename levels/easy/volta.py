import math

def main():
    x, y = map(int, input().split())
    
    r = math.ceil(y / (y - x))

    print(r)
    
    return 0

if __name__ == "__main__":
    main()
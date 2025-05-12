def subcadeia(p) -> bool:
    for i in range(len(p)):
        j = len(p) - 1 - i
        
        if i >= j:
            return True
        
        if p[i] == p[j]:
            continue
        
        return False
    return True
    
def main() -> int:
    n = int(input())
    p = str(input())
    
    max = float("-inf")
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = p[i:j + 1]
            
            if subcadeia(sub):
                max = len(sub) if len(sub) > max else max
    
    print(max)
    return 0
        
    
if __name__ == "__main__":
    main()

def mergeSort(arr):
    t = len(arr)

    if t < 2:
        return arr

    pivo = arr[0]

    menores = [x for x in arr[1:] if x <= pivo]
    maiores = [x for x in arr[1:] if x > pivo]

    return mergeSort(maiores) + [pivo] + mergeSort(menores)

def main():
    n = int(input())
    ns = list(map(int, input().split()))

    print(*mergeSort(ns))
    
    return 0

if __name__ == "__main__":
    main()
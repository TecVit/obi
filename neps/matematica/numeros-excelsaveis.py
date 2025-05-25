def main():
    n = int(input())
    ns = list(map(int, input().split()))
    so, sub, m, d = map(int, input().split())

    ns.sort()

    l = 0
    r = n - 1

    while l < r:

        if ns[l] * ns[r] > m:
            r -= 1
        elif ns[l] * ns[r] < m:
            l += 1
        else:
            # print("Multiplicacao: Certa")
            if ns[l] + ns[r] > so:
                r -= 1
            elif ns[l] + ns[r] < so:
                l += 1
            else:
                # print("Soma: Certa")
                if int(ns[r] / ns[l]) > d:
                    r -= 1
                elif int(ns[r] / ns[l]) < d:
                    l += 1
                else:
                    # print("Divisao: Certa")
                    if ns[r] - ns[l] > sub:
                        r -= 1
                    elif ns[r] - ns[l] < sub:
                        l += 1
                    else:
                        # print("Subtracao: Certa")
                        print(ns[l], ns[r])
                        return 0

    print(-1)
    return 0

if __name__ == "__main__":
    main()
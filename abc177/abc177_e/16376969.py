def main():
    import sys
    input = sys.stdin.buffer.readline
    from math import gcd
    N = int(input())
    A = list(map(int, input().split()))
    g = A[0]
    M = max(A)
    X = [i for i in range(M+1)]
    S = [True for i in range(M+1)]
    S[0] = False
    S[1] = False

    for i in range(1, M+1):
        if S[i]:
            for j in range(i, M+1, i):
                if S[j]:
                    S[j] = False
                    X[j] = i
    flag = True
    s = set()
    ls = 0
    for x in A:
        tmp = set()
        while(X[x] != 1):
            tmp.add(X[x])
            x //= X[x]
        l = len(tmp)
        s |= tmp
        if len(s) == ls + l:
            ls += l
            continue
        else:
            flag = False
            break

    if flag:
        print("pairwise coprime")
    else:
        for x in A[1:]:
            g = gcd(g, x)
        if g == 1:
            print("setwise coprime")

        else:
            print("not coprime")


main()

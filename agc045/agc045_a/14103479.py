def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        S = input()
        L = max(A).bit_length()
        s = [0]*L
        ID = A.index(max(A))

        def check(x):
            for i in range(L-1, -1, -1):
                if (x >> i) % 2:
                    x ^= s[i]
            return(x == 0)

        def update(x):
            flag = False
            if x.bit_length() == 60:
                flag = True
            for i in range(L-1, -1, -1):
                if (x >> i) % 2:
                    x ^= s[i]
            id = x.bit_length() - 1
            if id >= 0:
                s[id] = x

        res = 0
        L2 = 0
        for i in range(N-1, -1, -1):
            k = int(S[i])
            if k:
                if check(A[i]):
                    continue
                else:
                    res = 1
                    break
            else:
                L2 = max(L2, A[i].bit_length())
                update(A[i])
        print(res)



main()

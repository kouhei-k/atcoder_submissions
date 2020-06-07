def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        S = input()
        L = max(A).bit_length()
        s = [0]*L

        def check(x):
            for i in range(L-1, -1, -1):
                if (x >> i) % 2:
                    x ^= s[i]
            return(x == 0)

        def update(x):
            for i in range(L-1, -1, -1):
                if (x >> i) % 2:
                    x ^= s[i]
            id = x.bit_length() - 1
            if id >= 0:
                s[id] = x

        res = 0
        for i in range(N-1, -1, -1):
            k = int(S[i])
            if k:
                if check(A[i]):
                    continue
                else:
                    res = 1
                    break
            else:
                update(A[i])
        print(res)


main()

def main():
    import sys
    input = sys.stdin.buffer.readline
    import bisect
    N, T = map(int, input().split())

    A = list(map(int, input().split()))

    X = []
    Y = []

    n = N // 2
    ans = 0
    for i in range(2**n):
        tmp = 0
        for j in range(n):
            if (i >> j) % 2 == 1:
                tmp += A[j]
        if tmp <= T:
            if tmp > ans:
                ans = tmp
            X.append(tmp)
    n2 = N - n
    for i in range(2**n2):
        tmp = 0
        for j in range(n2):
            if (i >> j) % 2 == 1:
                tmp += A[n+j]
        if tmp <= T:
            if tmp > ans:
                ans = tmp
            Y.append(tmp)

    X.sort()
    Y.sort()
    n2 = len(Y)

    for x in X:
        tmp = 0
        id = bisect.bisect_left(Y, T - x)
        if id < n2 and x + Y[id] <= T:
            tmp = x + Y[id]
        else:
            tmp = x + Y[id-1]
        if tmp > ans:
            ans = tmp

    print(ans)


main()

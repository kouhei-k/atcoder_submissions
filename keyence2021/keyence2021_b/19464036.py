def main():
    import sys
    input = sys.stdin.buffer.readline
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    d = dict()
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    M = max(a)

    X = K
    ans = 0
    for i in range(M+1):
        if i in d:
            X = min(X, d[i])
            ans += X
        else:
            break
    print(ans)


main()

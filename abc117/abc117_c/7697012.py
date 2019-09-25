N, M = map(int, input().split())
X = list(map(int, input().split()))

if N >= M:
    print(0)
else:
    X.sort()
    spot = [0]*M
    diff = [[0, 0]]*(M-1)
    for i in range(M-1):
        diff[i] = [X[i+1]-X[i], i]
    diff.sort(key=lambda x: x[0])
    if N == 1:
        print(X[-1]-X[0])

    else:
        ans = X[-1] - X[0]
        for i in range(N-1):
            tmp = diff.pop()
            ans -= tmp[0]
        print(ans)

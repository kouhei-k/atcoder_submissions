def main():
    import collections
    import sys
    input = sys.stdin.buffer.readline
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for i in range(M)]
    K = int(input())
    C = list(map(int, input().split()))

    G = [set() for i in range(N)]
    for a, b in AB:
        a -= 1
        b -= 1
        G[a].add(b)
        G[b].add(a)

    # ans = -1

    X = [[-1]*(K+1) for i in range(K+1)]

    d = dict()
    for i in range(K):
        d[C[i]-1] = i + 1

    for i in range(K+1):
        X[i][i] = 0
        if i == 0:
            for j in range(K):
                X[i][j+1] = 1
        else:
            S = set()
            q = collections.deque()
            q.append((C[i-1]-1, 0))
            S.add(C[i-1]-1)
            while(q):
                x, c = q.popleft()
                # print(i, x, S, c)
                for y in G[x]:
                    if y not in S:
                        S.add(y)
                        if y in d:
                            X[i][d[y]] = c+1
                            X[d[y]][i] = c+1
                        q.append((y, c+1))
    # print(X)

    for i in range(1, K+1):
        if -1 in X[i][1:]:
            print(-1)
            exit(0)

    dp = [[-1]*(K+1) for i in range(2**K)]
    dp[0][0] = 0
    for i in range(K):
        dp[1 << i][i+1] = 1
    for i in range(1, 2**K):
        for j in range(K):
            if (i >> j) % 2 == 1:
                for k in range(K):
                    if j == k:
                        continue
                    if dp[i ^ (1 << j)][k+1] > 0:
                        # print(i, i ^ (1 << j), k, dp[i][j+1], dp[i ^ (1 << j)]
                        #       [k+1], X[k+1][j+1])
                        if dp[i][j+1] >= 0:
                            dp[i][j+1] = min(dp[i][j+1], dp[i ^ (1 << j)]
                                             [k+1]+X[k+1][j+1])
                        else:
                            dp[i][j+1] = dp[i ^ (1 << j)][k+1]+X[k+1][j+1]

    # print(dp)
    print(min(dp[-1][1:]))


main()

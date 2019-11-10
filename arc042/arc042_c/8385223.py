import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)
N, P = map(int, input().split())
ab = [tuple(map(int, input().split())) for i in range(N)]
ab.sort(key=lambda x: x[1])
ab.sort(key=lambda x: x[0])
dp = [[0]*(P+1) for i in range(N+1)]


ans = ab[0][1]
for i in reversed(range(1, N)):
    for j in range(P+1):
        if j < ab[i][0]:
            dp[i][j] = dp[i+1][j]
        else:
            dp[i][j] = max(dp[i+1][j], dp[i+1][j-ab[i][0]] + ab[i][1])
    tmp = dp[i][P] + ab[i-1][1]
    ans = max(ans, tmp)
print(ans)

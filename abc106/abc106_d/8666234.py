import collections
import bisect
import sys
input = sys.stdin.readline
N, M, Q = map(int, input().split())
LR = [tuple(map(int, input().split())) for i in range(M)]
dp = [[0]*(N+1) for i in range(N+1)]

for L, R in LR:
    dp[L][R] += 1
for i in reversed(range(1, N)):
    for j in range(1, N+1):
        dp[i][j] += dp[i+1][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] += dp[i][j-1]


for _ in range(Q):
    p, q = map(int, input().split())
    print(dp[p][q])

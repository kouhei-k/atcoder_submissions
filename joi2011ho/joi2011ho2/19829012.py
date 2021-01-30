import heapq
N, K = map(int, input().split())
A = [[] for i in range(10)]
for i in range(N):
    c, g = map(int, input().split())
    g -= 1

    A[g].append(c)
dp = [-1]*(K+1)
dp[0] = 0
for i in range(10):
    A[i].sort(reverse=True)
    L = len(A[i])
    SA = [0]*(L+1)
    for j in range(L):
        SA[j+1] = SA[j] + A[i][j] + j*2
    for j in range(K, 0, -1):
        for k in range(L):
            if j-k-1 < 0:
                break
            else:
                if dp[j-k-1] >= 0:
                    if dp[j] == -1:
                        dp[j] = dp[j-k-1] + SA[k+1]
                    elif dp[j] <= dp[j-k-1] + SA[k+1]:
                        dp[j] = dp[j-k-1]+SA[k+1]


print(dp[-1])

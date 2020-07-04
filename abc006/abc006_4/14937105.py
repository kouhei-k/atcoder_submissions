import bisect
N = int(input())
A = [int(input()) for i in range(N)]

ans = 0
s = set()
id = 0
dp = [0]
for i in range(N):
    id = bisect.bisect_right(dp, A[i])
    if id == len(dp):
        dp.append(A[i])
    else:
        if dp[id] > A[i]:
            dp[id] = A[i]

print(N - (len(dp)-1))

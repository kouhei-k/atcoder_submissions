import bisect
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

SA = [0]*(N+1)
SB = [0]*(M+1)
T = 0


ans = 0

for i in range(N):
    SA[i+1] = SA[i] + A[i]

for i in range(M):
    SB[i+1] = SB[i] + B[i]

for i in range(N+1):
    if SA[i] > K:
        break
    id = bisect.bisect_right(SB, K - SA[i]) - 1
    ans = max(ans, i + id)


print(ans)

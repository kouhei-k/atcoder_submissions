N, K = map(int, input().split())
A = list(map(int, input().split()))

count = [[0, 0] for i in range(N)]
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            count[i][0] += 1
    for j in range(i+1, N):
        if A[j] < A[i]:
            count[i][1] += 1
ans = 0
mod = 10**9 + 7

for i in range(N):
    ans += (1+K-1)*(K-1) // 2 * count[i][0]
    ans += (1+K)*K // 2 * count[i][1]
    ans %= mod

print(ans % mod)

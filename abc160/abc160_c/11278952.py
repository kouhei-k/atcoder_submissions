K, N = map(int, input().split())
A = list(map(int, input().split()))


ans = 10**12

for i in range(N):
    if i == 0:
        ans = min(ans, A[-1] - A[i])
    else:
        ans = min(ans, A[i-1] + (K - A[i]))

print(ans)

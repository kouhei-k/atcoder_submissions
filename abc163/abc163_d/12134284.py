N, K = map(int, input().split())
mod = 10**9 + 7
ans = 1

prev = 1
for k in range(1, N+1):
    prev = prev - (k-1) + N - (k-1)
    if k >= K:
        ans += prev
        ans %= mod


print(ans % mod)

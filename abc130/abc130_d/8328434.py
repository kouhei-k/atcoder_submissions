import bisect
N, K = map(int, input().split())
a = list(map(int, input().split()))

s = [0]*(N+1)
for i in range(N):
    s[i+1] = s[i] + a[i]
ans = 0
for i in range(1, N+1):
    if s[i] >= K:
        d = s[i] - K
        id = bisect.bisect_right(s, d)
        ans += min(max(id, 1), i)
print(ans)

import bisect
N, K = map(int, input().split())
a = list(map(int, input().split()))

s = [0]*(N+1)

for i in range(N):
    s[i+1] = s[i] + a[i]
ans = 0
for i in range(N):
    id = bisect.bisect_left(s, K + s[i])
    ans += (N-id)+1


# print(s)
print(ans)

N, K = map(int, input().split())
p = list(map(int, input().split()))

s = [0]*N
for i in range(N):
    s[i] = (p[i]+1) / 2
ss = [0]*(N+1)

for i in range(N):
    ss[i+1] = ss[i] + s[i]

ans = 0
for i in range(N - K + 1):
    ans = max(ans, ss[i+K] - ss[i])

print(ans)

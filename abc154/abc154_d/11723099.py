N, K = map(int, input().split())
p = list(map(int, input().split()))

P = [(1+p[i])/2 for i in range(N)]

ans = sum(P[:K])
tmp = ans
for i in range(N-K):
    tmp = tmp - P[i]+P[i+K]
    ans = max(ans, tmp)

print(ans)

N, M = map(int, input().split())
H = list(map(int, input().split()))

AB = [tuple(map(int, input().split())) for i in range(M)]
G = [0]*N

for a, b in AB:
    a -= 1
    b -= 1
    if G[a] < H[b]:
        G[a] = H[b]
    if G[b] < H[a]:
        G[b] = H[a]
ans = 0
for i in range(N):
    if H[i] > G[i]:
        ans += 1
print(ans)

H, W = map(int, input().split())
S = [input() for i in range(H)]

d = [0]*(H*W+1)
d[0] = 1
mod = 10**9 + 7
for i in range(H*W):
    d[i+1] = d[i]*2
    d[i+1] %= mod

D = [[0]*W for i in range(H)]
K = 0
for i in range(H):
    s = [0]*(W+1)
    cnt = 0
    prev = 0
    for j in range(W):
        if S[i][j] == '.':
            K += 1
            cnt += 1
        else:
            s[prev] = cnt
            s[j] = -cnt
            prev = j+1
            cnt = 0
    if cnt > 0:
        s[prev] = cnt
    c = 0
    for j in range(W):
        c += s[j]
        D[i][j] += c

for j, x in enumerate(zip(*S)):
    s = [0]*(H+1)
    cnt = 0
    prev = 0
    for i, y in enumerate(x):
        if y == '.':
            cnt += 1
        else:
            s[prev] = cnt
            s[i] = -cnt
            prev = i+1
            cnt = 0
    if cnt > 0:
        s[prev] = cnt
    c = 0
    for i in range(H):
        c += s[i]
        D[i][j] += c
ans = 0
for i in range(H):
    for j, x in enumerate(D[i]):
        if S[i][j] == '.':
            x -= 1
        if x > 0:
            ans += (d[x]-1)*d[K-x]
            ans %= mod
print(ans % mod)

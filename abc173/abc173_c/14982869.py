H, W, K = map(int, input().split())
c = [list(input()) for i in range(H)]

ans = 0

for i in range(2**(H+W)):
    h = set()
    for j in range(H):
        if (i >> j) % 2 == 1:
            h.add(j)
    w = set()
    for j in range(W):
        if (i >> (j + H)) % 2 == 1:
            w.add(j)
    tmp = 0
    for j in range(H):
        if j in h:
            continue
        for k in range(W):
            if k in w:
                continue
            if c[j][k] == '#':
                tmp += 1

    if tmp == K:
        ans += 1

print(ans)

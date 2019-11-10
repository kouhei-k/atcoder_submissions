from collections import deque
H, W = map(int, input().split())
s = [list(input()) for i in range(H)]

white = 0

for i in range(H):
    white += s[i].count(".")

q = deque()
q.append((0, 0))

g = [[10**9]*W for i in range(H)]
g[0][0] = 0
for i in range(H*W):
    if len(q) == 0:
        break
    x, y = q.popleft()
    if (x, y) == (H-1, W-1):
        break
    else:
        if x < H-1 and s[x+1][y] == ".":
            if g[x+1][y] == 10**9:
                q.append((x+1, y))
            g[x+1][y] = min(g[x+1][y], g[x][y]+1)
        if y < W-1 and s[x][y+1] == ".":
            if g[x][y+1] == 10**9:
                q.append((x, y+1))
            g[x][y+1] = min(g[x][y+1], g[x][y]+1)
        if x > 0 and s[x-1][y] == ".":
            if g[x-1][y] == 10**9:
                q.append((x-1, y))
            g[x-1][y] = min(g[x-1][y], g[x][y]+1)
        if y > 0 and s[x][y-1] == ".":
            if g[x][y-1] == 10**9:
                q.append((x, y-1))
            g[x][y-1] = min(g[x][y-1], g[x][y]+1)
if g[H-1][W-1] == 10**9:
    print(-1)
else:
    print(white - (g[H-1][W-1]+1))

import collections
H, W = map(int, input().split())
s = [list(input()) for i in range(H)]

ans = H*W - 2
for i in range(H):
    for j in range(W):
        if s[i][j] == "#":
            ans -= 1
q = collections.deque()
q.append((0, 0, 0))
flag = False
while(q):
    x, y, d = q.popleft()
    if x == W-1 and y == H - 1:
        ans -= (d-1)
        flag = True
        break
    if y > 0 and s[y-1][x] == ".":
        q.append((x, y-1, d+1))
        s[y-1][x] = "#"
    if x > 0 and s[y][x-1] == ".":
        q.append((x-1, y, d+1))
        s[y][x-1] = "#"
    if y < H - 1 and s[y+1][x] == ".":
        q.append((x, y+1, d+1))
        s[y+1][x] = "#"
    if x < W - 1 and s[y][x+1] == ".":
        q.append((x+1, y, d+1))
        s[y][x+1] = "#"

if flag:
    print(ans)
else:
    print(-1)

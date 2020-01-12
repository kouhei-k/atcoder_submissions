import collections
H, W = map(int, input().split())
S = [list(input()) for i in range(H)]
q = collections.deque()
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        q.append((i, j))
        tmp = [[-1]*W for i in range(H)]
        tmp[i][j] = 0
        while(q):
            y, x = q.popleft()
            if y > 0 and tmp[y-1][x] < 0 and S[y-1][x] != "#":
                q.append((y-1, x))
                tmp[y-1][x] = tmp[y][x] + 1
                ans = max(ans, tmp[y-1][x])
            if y < H-1 and tmp[y+1][x] < 0 and S[y+1][x] != "#":
                q.append((y+1, x))
                tmp[y+1][x] = tmp[y][x] + 1
                ans = max(ans, tmp[y+1][x])
            if x > 0 and tmp[y][x-1] < 0 and S[y][x-1] != "#":
                q.append((y, x-1))
                tmp[y][x-1] = tmp[y][x] + 1
                ans = max(ans, tmp[y][x-1])
            if x < W - 1 and tmp[y][x+1] < 0 and S[y][x+1] != "#":
                q.append((y, x+1))
                tmp[y][x+1] = tmp[y][x] + 1
                ans = max(ans, tmp[y][x+1])
print(ans)

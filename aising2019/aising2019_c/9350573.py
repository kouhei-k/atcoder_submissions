import collections
H, W = map(int, input().split())
S = [list(input()) for i in range(H)]

remaining = set()
for i in range(H):
    for j in range(W):
        remaining.add((i, j))

q = collections.deque()
ans = 0
while(remaining):
    i, j = remaining.pop()
    q.append((i, j))
    black = 0
    white = 0
    while(q):
        y, x = q.popleft()
        if S[y][x] == "#":
            black += 1
        else:
            white += 1

        if (y-1, x) in remaining and S[y][x] != S[y-1][x]:
            remaining.remove((y-1, x))
            q.append((y-1, x))
        if (y, x-1) in remaining and S[y][x] != S[y][x-1]:
            remaining.remove((y, x-1))
            q.append((y, x-1))
        if (y+1, x) in remaining and S[y][x] != S[y+1][x]:
            remaining.remove((y+1, x))
            q.append((y+1, x))
        if (y, x+1) in remaining and S[y][x] != S[y][x+1]:
            remaining.remove((y, x+1))
            q.append((y, x+1))
    ans += black * white
print(ans)

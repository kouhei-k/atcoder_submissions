import collections
H, W = map(int, input().split())
c = [list(input()) for i in range(H)]
sx, sy = 0, 0
gx, gy = 0, 0
for i in range(H):
    for j in range(W):
        if c[i][j] == "s":
            sx = i
            sy = j
        elif c[i][j] == "g":
            gx = i
            gy = j
q = collections.deque()

q.append((sx, sy))
flag = False
C = [[1]*W for i in range(H)]
C[sx][sy] = 0
S1 = set()
S2 = set()
while(q):
    x, y = q.popleft()
    if x == gx and y == gy:
        flag = True
        break
    else:
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if x2 >= 0 and y2 >= 0 and x2 < H and y2 < W:
                if c[x2][y2] == '#':
                    S1.add((x2, y2))
                else:
                    if C[x2][y2]:
                        C[x2][y2] = 0
                        q.append((x2, y2))

if flag:
    print("YES")
else:
    q.append((gx, gy))
    while(q):
        x, y = q.popleft()
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if x2 >= 0 and y2 >= 0 and x2 < H and y2 < W:
                if c[x2][y2] == '#':
                    S2.add((x2, y2))
                else:
                    if C[x2][y2]:
                        C[x2][y2] = 0
                        q.append((x2, y2))
    if len(S1 & S2) > 0:
        print("YES")
        exit(0)
    else:
        for i, j in S1:
            q.append((i, j))
            S3 = set()
            while(q):
                x, y = q.popleft()
                for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if x2 >= 0 and y2 >= 0 and x2 < H and y2 < W:
                        if c[x2][y2] == '#':
                            S3.add((x2, y2))
                        else:
                            if C[x2][y2]:
                                C[x2][y2] = 0
                                q.append((x2, y2))
            if len(S2 & S3) > 0:
                print("YES")
                exit(0)
    print("NO")

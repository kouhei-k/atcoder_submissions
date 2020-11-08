H, W, N, M = map(int, input().split())

AB = [tuple(map(int, input().split())) for i in range(N)]
CD = [tuple(map(int, input().split())) for i in range(M)]


AB = set(AB)

CD = set(CD)

G = [[0]*(W+1) for i in range(H+1)]
G2 = [[0]*(W+1) for i in range(H+1)]
for i, j in AB:
    G[i][j] = 1
    G2[i][j] = 1
for i, j in CD:
    G[i][j] = -1
    G2[i][j] = -1


ans = 0
while(AB):
    i, j = AB.pop()

    for k in range(i+1, H+1):
        if G[k][j] == 0:
            G[k][j] = 1
        else:
            break
    for k in range(i-1, 0, -1):
        if G[k][j] == 0:
            G[k][j] = 1
        else:
            break
    for k in range(j+1, W+1):
        if G2[i][k] == 0:
            G2[i][k] = 1
        else:
            break
    for k in range(j-1, 0, -1):
        if G2[i][k] == 0:
            G2[i][k] = 1
        else:
            break
for i in range(1, H+1):
    for j in range(1, W+1):
        if G[i][j] == 1 or G2[i][j] == 1:
            ans += 1

print(ans)

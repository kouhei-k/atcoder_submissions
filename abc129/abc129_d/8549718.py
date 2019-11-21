H, W = map(int, input().split())
grid = [list(input()) for i in range(H)]

grid2 = [[0]*W for i in range(H)]
grid3 = [[0]*W for i in range(H)]
for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            grid2[i][j] = 0
        else:
            if j > 0:
                grid2[i][j] = grid2[i][j-1]+1
            else:
                grid2[i][j] = 1
    for j in reversed(range(W)):
        if grid2[i][j] != 0 and j != W-1:
            grid2[i][j] = max(grid2[i][j], grid2[i][j+1])

for j in range(W):
    for i in range(H):
        if grid[i][j] == "#":
            grid3[i][j] = 0
        else:
            if i > 0:
                grid3[i][j] = grid3[i-1][j]+1
            else:
                grid3[i][j] = 1
    for i in reversed(range(H)):
        if grid3[i][j] != 0 and i != H-1:
            grid3[i][j] = max(grid3[i][j], grid3[i+1][j])
ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, grid2[i][j] + grid3[i][j] - 1)

print(ans)

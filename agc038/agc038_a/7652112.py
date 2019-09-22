H, W, A, B = map(int, input().split())
grid = [[0]*W for i in range(H)]

for i in range(H - B):
    grid[i][W - A:] = [1] * A

for i in range(H - B, H):
    grid[i][:W - A] = [1] * (W - A)
for i in range(H):
    print("".join(map(str, grid[i])))

H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))
grid = [[0] * W for i in range(H)]
count = 0
reverse = False
for i in range(H):
    if reverse:
        for j in reversed(range(W)):
            if a[count] == 0:
                count += 1
            grid[i][j] = count+1
            a[count] -= 1
        reverse = False
    else:
        for j in range(W):
            if a[count] == 0:
                count += 1
            grid[i][j] = count+1
            a[count] -= 1

        reverse = True


for i in range(H):
    print(" ".join(map(str, grid[i])))

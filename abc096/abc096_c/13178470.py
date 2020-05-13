H, W = map(int, input().split())
s = [input() for i in range(H)]
for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            if i > 0 and s[i-1][j] == '#':
                continue
            elif i < H-1 and s[i+1][j] == '#':
                continue
            elif j > 0 and s[i][j-1] == '#':
                continue
            elif j < W-1 and s[i][j+1] == '#':
                continue
            else:
                print("No")
                exit(0)
print("Yes")

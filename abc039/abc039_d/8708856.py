H, W = map(int, input().split())
S = [list(input()) for i in range(H)]
ans = [["."]*W for i in range(H)]
check = [["."]*W for i in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            continue
        else:
            if i > 0 and i < H - 1:
                if j > 0 and j < W - 1:
                    if S[i+1][j+1] == "#" and S[i+1][j] == "#" and S[i][j+1] == "#" and S[i-1][j+1] == "#" and S[i+1][j-1] == "#" and S[i-1][j] == "#" and S[i][j-1] == "#" and S[i-1][j-1] == "#":
                        ans[i][j] = "#"
                elif j == W - 1:
                    if S[i+1][j] == "#" and S[i+1][j-1] == "#" and S[i-1][j] == "#" and S[i][j-1] == "#" and S[i-1][j-1] == "#":
                        ans[i][j] = "#"
                elif j == 0 :
                    if S[i+1][j] == "#" and S[i+1][j+1] == "#" and S[i-1][j] == "#" and S[i][j+1] == "#" and S[i-1][j+1] == "#":
                        ans[i][j] = "#"
            elif i == H - 1:
                if j > 0 and j < W - 1:
                    if S[i][j+1] == "#" and S[i-1][j+1] == "#" and S[i-1][j] == "#" and S[i][j-1] == "#" and S[i-1][j-1] == "#":
                        ans[i][j] = "#"
                elif j == W - 1:
                    if S[i][j-1] == "#" and S[i-1][j-1] == "#" and S[i-1][j] == "#":
                        ans[i][j] = "#"
                elif j == 0:
                    if S[i][j+1] == "#" and S[i-1][j+1] == "#" and S[i-1][j] == "#":
                        ans[i][j] = "#"
            elif i == 0:
                if j > 0 and j < W - 1:
                    if S[i][j+1] == "#" and S[i+1][j+1] == "#" and S[i+1][j] == "#" and S[i][j-1] == "#" and S[i+1][j-1] == "#":
                        ans[i][j] = "#"
                elif j == W - 1:
                    if S[i][j-1] == "#" and S[i+1][j-1] == "#" and S[i+1][j] == "#":
                        ans[i][j] = "#"
                elif j == 0:
                    if S[i][j+1] == "#" and S[i+1][j+1] == "#" and S[i+1][j] == "#":
                        ans[i][j] = "#"

for i in range(H):
    for j in range(W):
        if ans[i][j] == "#":
            check[i][j] = "#"
            if j > 0:
                check[i][j-1] = "#"
            if j < W - 1:
                check[i][j+1] = "#"
            if i > 0:
                check[i-1][j] = "#"
                if j > 0:
                    check[i-1][j-1] = "#"
                if j < W - 1:
                    check[i-1][j+1] = "#"

            if i < H - 1:
                check[i+1][j] = "#"
                if j > 0:
                    check[i+1][j-1] = "#"
                if j < W - 1:
                    check[i+1][j+1] = "#"
if check == S:
    print("possible")
    for i in range(H):
        print("".join(ans[i]))
else:
    print("impossible")

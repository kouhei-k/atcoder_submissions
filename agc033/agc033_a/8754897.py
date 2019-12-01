import collections
import sys
input = sys.stdin.readline
H, W = map(int, input().split())
A = [list(input()) for i in range(H)]
dp = [[H+W]*W for i in range(H)]

q = collections.deque()
for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
            dp[i][j] = 0
            q.append([i, j])
            break
    if q:
        break


while(q):
    x, y = q.popleft()
    if x > 0:
        if dp[x-1][y] > dp[x][y]+1:
            if A[x-1][y] == ".":
                dp[x-1][y] = dp[x][y]+1
            else:
                dp[x-1][y] = 0
            q.append([x-1, y])
    if x < H-1:
        if dp[x+1][y] > dp[x][y]+1:
            if A[x+1][y] == ".":
                dp[x+1][y] = dp[x][y]+1
            else:
                dp[x+1][y] = 0
            q.append([x+1, y])
    if y > 0:
        if dp[x][y-1] > dp[x][y]+1:
            if A[x][y-1] == ".":
                dp[x][y-1] = dp[x][y]+1
            else:
                dp[x][y-1] = 0
            q.append([x, y-1])
    if y < W-1:
        if dp[x][y+1] > dp[x][y]+1:
            if A[x][y+1] == ".":
                dp[x][y+1] = dp[x][y]+1
            else:
                dp[x][y+1] = 0
            q.append([x, y+1])
ans = 0
for i in range(H):
    ans = max(ans, max(dp[i]))
print(ans)

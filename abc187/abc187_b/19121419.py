N = int(input())
xy = [tuple(map(int, input().split())) for i in range(N)]
ans = 0
for i in range(N-1):
    x, y = xy[i]
    for j in range(i+1, N):
        x2, y2 = xy[j]
        k = (y2-y) / (x2 - x)
        if -1 <= k <= 1:
            ans += 1
print(ans)

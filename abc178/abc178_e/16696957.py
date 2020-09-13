N = int(input())
xy = [tuple(map(int, input().split())) for i in range(N)]

F = [0]*N

for i in range(N):
    F[i] = xy[i][0] - xy[i][1]
ans = max(F) - min(F)

for i in range(N):
    F[i] = xy[i][0] + xy[i][1]
ans2 = max(F) - min(F)

print(max(ans, ans2))

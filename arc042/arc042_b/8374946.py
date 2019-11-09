x, y = map(int, input().split())
N = int(input())
xy = [list(map(int, input().split())) for i in range(N)]
ans = 10**9
for i in range(1, N):
    a = 0
    if xy[i][0] - xy[i-1][0] != 0:
        a = (xy[i][1] - xy[i-1][1])/(xy[i][0] - xy[i-1][0])
    c = xy[i][1] - a * xy[i][0]

    d = abs(a*x-y+c) / (a**2 + 1)**0.5

    ans = min(ans, d)
a = 0
if xy[0][0] - xy[N-1][0] != 0:
    a = (xy[0][1] - xy[N-1][1])/(xy[0][0] - xy[N-1][0])
    c = xy[0][1] - a*xy[0][0]
    d = abs(a*x-y+c) / (a**2 + 1)**0.5

    ans = min(ans, d)
print(ans)

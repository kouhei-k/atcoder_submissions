N, D = map(int, input().split())
XY = [tuple(map(int, input().split())) for i in range(N)]
D *= D
ans = 0
for x, y in XY:
    if x**2 + y**2 <= D:
        ans += 1
print(ans)

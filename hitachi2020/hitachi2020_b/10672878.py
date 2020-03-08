A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
xyc = [tuple(map(int, input().split())) for i in range(M)]

ans = min(a) + min(b)

for x, y, c in xyc:
    x -= 1
    y -= 1
    ans = min(ans, a[x]+b[y] - c)
print(ans)

N, x = map(int, input().split())
a = list(map(int, input().split()))

m = min(a)
ans = 0
if a[0] > x:
    ans += a[0] - x
    a[0] = x
for i in range(1, N):
    if a[i] + a[i-1] > x:
        tmp = x - a[i - 1]
        ans += a[i] - tmp
        a[i] = tmp

print(ans)

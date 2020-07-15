N = int(input())
XL = [tuple(map(int, input().split())) for i in range(N)]

XL.sort(key=lambda x: x[0] + x[1])
ans = 0
prev = - 10**9
for x, l in XL:
    if prev <= x - l:
        ans += 1
        prev = x + l

print(ans)

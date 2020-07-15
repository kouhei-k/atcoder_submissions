N, T = map(int, input().split())
t = list(map(int, input().split()))

ans = 0
end = -1
start = -1
for x in t:
    if end < x:
        ans += (end - start)
        start = x
        end = x + T
    else:
        end = x + T

ans += (end - start)

print(ans)

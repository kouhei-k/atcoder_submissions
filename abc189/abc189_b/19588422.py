N, X = map(int, input().split())
VP = [tuple(map(int, input().split())) for i in range(N)]

ans = -1
x = 0
X *= 100
for i in range(N):
    v, p = VP[i]
    x += v * p
    if x > X:
        ans = i+1
        break
print(ans)

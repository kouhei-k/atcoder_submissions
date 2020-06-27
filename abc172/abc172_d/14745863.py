N = int(input())

ans = 0
for i in range(1, N+1):
    k = N // i
    sk = (i + i*k)*k // 2
    ans += sk
print(ans)

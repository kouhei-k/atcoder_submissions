N = int(input())
B = list(map(int, input().split()))

ans = 0
for i in range(N - 1):
    if i == N - 2:
        ans += B[i]
    else:
        ans += min(B[i], B[i+1])

ans += B[0]
print(ans)

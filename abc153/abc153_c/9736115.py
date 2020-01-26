N, K = map(int, input().split())
H = list(map(int, input().split()))

ans = 0
H.sort(reverse=True)
for i in range(N):
    if K > 0:
        K -= 1
    else:
        ans += H[i]
print(ans)

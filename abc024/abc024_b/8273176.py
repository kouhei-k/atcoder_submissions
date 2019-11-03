N, T = map(int, input().split())
A = [int(input()) for i in range(N)]
ans = 0
l = 0
for i in range(N):
    if A[i] < l:
        ans -= l - A[i]
    ans += T
    l = A[i] + T
print(ans)

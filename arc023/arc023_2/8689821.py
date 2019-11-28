R, C, D = map(int, input().split())
A = [list(map(int, input().split())) for i in range(R)]

dp = [[-1] * C for i in range(R)]
k = D % 2
ans = 0
for i in reversed(range(R)):
    for j in reversed(range(C)):
        if i + j <= D and (i+j) % 2 == k:
            ans = max(ans, A[i][j])
print(ans)

m, n = map(int, input().split())
a, b = map(int, input().split())
c = [list(map(int, input().split())) for i in range(n)]

S = [[0]*(m+1) for i in range(n+1)]

for i in range(n):
    for j in range(m):
        if c[i][j] >= 0:
            S[i+1][j+1] = S[i+1][j] + S[i][j+1] - S[i][j] + c[i][j]
        else:
            S[i+1][j+1] = S[i+1][j] + S[i][j+1] - S[i][j] + 100*a*b


ans = a*b*100
for i in range(n-b+1):
    for j in range(m-a+1):
        tmp = S[i+b][j+a]+S[i][j] - S[i][j+a] - S[i+b][j]
        if tmp < ans:
            ans = tmp
print(ans)

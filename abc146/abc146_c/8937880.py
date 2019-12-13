A, B, X = map(int, input().split())

minN = 1
maxN = 10**9
ans = 0
while(1):

    N = (minN + maxN) // 2
    n = A*N + len(str(N))*B
    if n <= X:
        ans = N
    if minN == maxN:
        break
    if n < X:
        minN = N+1
    else:
        maxN = N


print(ans)

N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for i in range(N)]
ans = 10**9
for i in range(1, 2**N):
    tmp = 0
    S = [0]*M
    for j in range(N):
        if(i >> j) % 2 == 1:
            tmp += CA[j][0]
            for k in range(M):
                S[k] += CA[j][k+1]
        if min(S) >= X:
            ans = min(ans, tmp)
if ans == 10**9:
    print(-1)
else:
    print(ans)

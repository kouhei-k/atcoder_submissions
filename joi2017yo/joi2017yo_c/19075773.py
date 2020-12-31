N, M, D = map(int, input().split())
S = [input() for i in range(N)]
ans = 0
for i in range(N):
    for j in range(M-D+1):
        flag = True
        for k in range(D):
            if S[i][j+k] == '.':
                continue
            else:
                flag = False
                break
        if flag:
            ans += 1

for i in range(M):
    for j in range(N-D+1):
        flag = True
        for k in range(D):
            if S[j+k][i] == '.':
                continue
            else:
                flag = False
                break
        if flag:
            ans += 1
print(ans)

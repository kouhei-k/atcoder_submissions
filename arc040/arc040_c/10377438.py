N = int(input())
S = [input() for i in range(N)]

G = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            G[i][j] = 1
ans = 0
for i in range(N):
    flag = False
    for j in range(N-1, -1, -1):
        if G[i][j] == 1:
            continue
        else:
            flag = True
            ans += 1
            if i < N-1:
                for k in range(j, N):
                    G[i+1][k] = 1
        if flag:
            break
print(ans)

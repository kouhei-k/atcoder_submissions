N = int(input())
s = [list(input()) for i in range(N)]
t = [["o"]*N for i in range(N)]

for i in range(N):
    for j in range(N):
        t[i][j] = s[N-1-j][i]

    print("".join(t[i]))

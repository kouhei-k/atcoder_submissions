N, A = map(int, input().split())
S = input()
ans = 0
L = A
R = A
x = 1
p = A
X = []
for i in range(N):
    if S[i] == '#':
        X.append(i)


while(L > X[0]+1 or R < X[-1]+1):
    if x:
        if R < N+1:
            R += 1
        ans += (R-p)
        if R == N+1:
            x = 0
        elif S[R-1] == '#':
            x = 0
        p = R
    else:
        if L > 0:
            L -= 1
        ans += (p - L)
        if L == 0:
            x = 1
        elif S[L-1] == '#':
            x = 1
        p = L


print(ans)

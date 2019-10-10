N = int(input())
S = input()


black = [0]*(N+1)
for i in range(N):
    if S[i] == "#":
        black[i+1] = black[i]+1
    else:
        black[i+1] = black[i]

ans = N
for i in range(N+1):
    tmp = (black[N-i]-black[0])+(i-(black[N]-black[N-i]))
    ans = min(tmp, ans)
print(ans)

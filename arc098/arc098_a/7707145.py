N = int(input())
S = list(input())

s = [0]*(N+1)
e = [0]*(N+1)
for i in range(1, N+1):
    k = 0
    if S[i-1] == "W":
        k = 1
    s[i] = s[i-1] + k

for i in reversed(range(0, N)):
    k = 0
    if S[i] == "E":
        k = 1
    e[i] = e[i+1] + k

ans = N
for i in range(1, N+1):
    ans = min(ans, s[i-1]+e[i])


print(ans)

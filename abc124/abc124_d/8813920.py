N, K = map(int, input().split())
S = list(input())
S = list(map(int, S))
s = []
tmp = 0

for i in range(N):
    if S[i] == 1:
        if tmp != 0:
            s.append((tmp, i-1))
        tmp = 0
    else:
        tmp += 1
        if i == N-1:
            s.append((tmp, i))
if len(s) <= K:
    print(N)
    exit(0)
ans = 0
for i in range(len(s)-K+1):
    tmp = 0
    if i+K == len(s):
        tmp = N-1
    else:
        tmp = s[i+K][1]-s[i+K][0]

    if i != 0:
        tmp -= s[i-1][1]
    else:
        tmp += 1
    ans = max(ans, tmp)

print(ans)

n, k = map(int, input().split())
c = [int(input()) for i in range(k)]

c.sort()
flag = False
if c[0] == 0:
    flag = True

S = []
l = -1
r = 0
for i in range(k):
    if c[i] == 0:
        continue
    else:
        if l < 0:
            l = c[i]
            r = c[i]
        elif c[i] == r+1:
            r += 1
        else:
            S.append((l, r))
            l = c[i]
            r = c[i]
S.append((l, r))
L = len(S)
ans = 0
if flag:
    for i in range(L-1):
        if S[i+1][0] - S[i][1] == 2:
            ans = max(ans, S[i+1][1] - S[i][0] + 1)

for a, b in S:
    ans = max(ans, b-a+1)
print(ans)

import collections
S = list(map(int, list(input())))
N = len(S)

dp = [0]*N
if N < 4:
    print(0)
    exit(0)

ans = 0

D = [0]*N
D[0] = 1
for i in range(1, N):
    D[i] = D[i-1]*10 % 2019
t = collections.defaultdict(int)
tmp = 0

t[0] += 1
for i in range(N):
    tmp += S[N-1-i]*D[i]
    tmp %= 2019
    t[tmp] += 1

for x in t:
    ans += t[x]*(t[x]-1) // 2

# print(N)
# print(*dp, sep='
')

print(ans)

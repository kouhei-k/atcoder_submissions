S = input()
N = len(S)
dp = [0]*(N+1)
ans = 0
d = dict()
d[0] = 1
dp = [0]*(N+1)
k = 1
for i in range(N):
    dp[i+1] = (dp[i] + int(S[N-i - 1]) * k) % 2019
    k *= 10
    k %= 2019
    if dp[i+1] in d:
        d[dp[i+1]] += 1
    else:
        d[dp[i+1]] = 1


for x in d:
    ans += (d[x]*(d[x]-1)) // 2
print(ans)

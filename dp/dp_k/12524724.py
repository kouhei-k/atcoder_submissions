N, K = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
ans = ['First', 'Second']

dp = [1]*(K+1)

for i in range(K+1):
    if i < a[0]:
        dp[i] = 1
    else:
        flag = False
        for x in a:
            if i-x >= 0 and dp[i-x]:
                dp[i] = 0
                flag = True
                break

print(ans[dp[-1]])

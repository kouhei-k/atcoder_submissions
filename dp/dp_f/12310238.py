s = input()
t = input()

dp = [[0]*len(t) for i in range(len(s))]


for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            if i > 0 and j > 0:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 1
        else:
            if i > 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j])
            if j > 0:
                dp[i][j] = max(dp[i][j-1], dp[i][j])


ret = ['']*dp[-1][-1]
id = dp[-1][-1]
i = len(s) - 1
j = len(t) - 1
while(i >= 0 and j >= 0):
    #print(s[i], t[j], i, j)
    if s[i] == t[j]:
        id -= 1
        ret[id] = s[i]
        i -= 1
        j -= 1
        # print(ret)
    else:
        if i > 0 and dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1

print(''.join(ret))
#print(*dp, sep='
')

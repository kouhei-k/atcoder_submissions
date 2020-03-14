N = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"

dp = [-1]*N
dp[0] = 1


ans = []


def solve(x, n, l):  # n:種類
    if l == N:
        ans.append(x)
    else:
        for i in range(n):
            j = n
            if i == n-1:
                j += 1
            solve(x + alpha[i], j, l+1)


solve("", 1, 0)
ans.sort()
for x in ans:
    print(x)

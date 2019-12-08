import bisect
N, M = map(int, input().split())
A = list(map(int, input().split()))
num = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
num = [(i, num[i]) for i in range(10) if i in A]
num.sort(key=lambda x: x[0], reverse=True)
num.sort(key=lambda x: x[1])
dp = [0 for i in range(N+1)]
ans = 0
tmp = set()
tmp.add(0)
for i in range(1, N+1):
    for n, k in num:
        if i - k in tmp:
            dp[i] = 1 + dp[i-k]
            tmp.add(i)
            break


num.sort(reverse=True)
tmp = N
ans = []
for i in reversed(range(1, dp[N])):
    for n, k in num:
        if dp[tmp - k] == i:
            ans.append(n)
            tmp -= k
            break
for n, k in num:
    if k == tmp:
        ans.append(n)
        break

ans.sort(reverse=True)
ans = "".join(map(str, ans))
print(ans)

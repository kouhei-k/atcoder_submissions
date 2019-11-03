import collections
import sys
sys.setrecursionlimit(2000)
N = int(input())
a, b = map(int, input().split())
M = int(input())
xy = [list(map(int, input().split())) for i in range(M)]
table = collections.defaultdict(list)
for i in range(M):
    table[xy[i][0]-1].append(xy[i][1]-1)
    table[xy[i][1]-1].append(xy[i][0]-1)
dp = [10**9]*N
dp[a-1] = 0
num = [0]*N
num[a-1] = 1
mod = 10**9 + 7


def solve(node, reached):
    if dp[node] != 10**9:
        return dp[node]

    else:
        reached.append(node)
        for x in table[node]:
            if x in reached:
                continue
            tmp = reached[:]
            ret = solve(x, tmp)
            if dp[node] > ret+1:
                dp[node] = ret+1
                num[node] = num[x]
            elif dp[node] == ret+1:
                num[node] += num[x] % mod

    return(dp[node])


solve(b-1, [])
print(num[b-1] % mod)

import sys
sys.setrecursionlimit(10**5)
N = int(input())
S = input()
T = [input() for i in range(N)]

mod = 10**9+7
dp = [-1]*(len(S)+1)
dp[-1] = 1


def solve(s):

    ret = 0
    if dp[-len(s)-1] > 0:
        return(dp[-len(s)-1])
    else:
        for x in T:
            if s.startswith(x):
                ret += solve(s[len(x):])
                ret %= mod
        dp[-len(s)-1] = ret
        return(ret)


ans = solve(S)
print(ans)

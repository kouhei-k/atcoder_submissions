import sys
sys.setrecursionlimit(10**6)


inf = float('Inf')
f = [2, 3, 5]
cost = [0]*4


d = dict()


def dfs(x, d):
    if x in d:
        return(d[x])
    ret = cost[-1]*x
    for i in range(3):
        if x < f[i]:
            continue
        if x % f[i] == 0:
            ret = min(ret, dfs(x // f[i], d) + cost[i])
        else:
            k = x // f[i]
            ret = min(ret, cost[i] + dfs(k, d) + (x %
                                                  f[i]) * cost[-1], cost[i] + dfs(k+1, d) + ((k+1)*f[i]-x)*cost[-1])
    d[x] = ret
    return(ret)


def main():
    T = int(input())
    for _ in range(T):
        N, *c = map(int, input().split())
        for i in range(4):
            cost[i] = c[i]
        print(dfs(N, dict()))


main()

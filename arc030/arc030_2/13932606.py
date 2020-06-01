import collections
n, x = map(int, input().split())
p = list(map(int, input().split()))
G = [set() for i in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].add(v)
    G[v].add(u)
x -= 1

q = collections.deque()
q.append((x, 0))
r = set([x])


def dfs(x, d, r):
    ret = 0
    if p[x]:
        ret = d

    for y in G[x]:
        if y in r:
            continue
        else:
            if ret > 0:
                d = 0
            ret += dfs(y, d+1, r | set([y]))
    return(ret)


print(dfs(x, 0, set([x])) * 2)

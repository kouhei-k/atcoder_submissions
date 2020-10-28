n = int(input())
m = int(input())

parent = [i for i in range(n)]


def root(x):
    if parent[x] == x:
        return(x)
    else:
        parent[x] = root(parent[x])
        return(parent[x])


def same(x, y):
    x = root(x)
    y = root(y)
    return(x == y)


def unite(x, y):
    if same(x, y):
        return
    else:
        x = root(x)
        y = root(x)
        parent[x] = y


S = [set() for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    S[a].add(b)
    S[b].add(a)

ans = set()
ans |= S[0]
# print(S)
for x in S[0]:
    ans |= S[x]
    # print(ans, S[x], x)
if 0 in ans:
    ans.remove(0)

print(len(ans))

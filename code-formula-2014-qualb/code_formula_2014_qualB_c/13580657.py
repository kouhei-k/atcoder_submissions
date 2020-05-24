import collections
A = list(input())
B = list(input())

a = collections.defaultdict(set)
b = collections.defaultdict(set)

aa = set()
ma = 0


for i, xy in enumerate(zip(A, B)):
    x, y = xy
    a[x].add(i)
    b[y].add(i)
    if x != y:
        aa.add(i)
if len(aa) > 6:
    print("NO")
    exit(0)

ma = 0
for x in A:
    if len(a[x]) == len(b[x]):
        ma = max(ma, len(a[x]))
        continue
    else:
        print("NO")
        exit(0)


def dfs(s, g, c):
    if c == 0:
        if ''.join(s) == ''.join(g):
            return(True)
        else:
            return(False)
    else:
        if ''.join(s) == ''.join(g):
            if ma > 1 or c == 2:
                return(True)
            else:
                return(False)
        else:
            l = len(s)
            for i in range(l):
                for j in range(i+1, l):
                    tmp = list(s[:])
                    tmp[i], tmp[j] = tmp[j], tmp[i]
                    if dfs(tmp, g, c-1):
                        return(True)
            return(False)


start = []
goal = []

for i in aa:
    start.append(A[i])
    goal.append(B[i])
if dfs(start, goal, 3):
    print("YES")
else:
    print("NO")

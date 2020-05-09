import collections
N = int(input())
s = [input() for i in range(N)]
M = int(input())
t = [input() for i in range(M)]

d = collections.defaultdict(int)
for x in s:
    d[x] += 1
for x in t:
    d[x] -= 1

ans = 0
for x in d:
    ans = max(ans, d[x])
print(ans)

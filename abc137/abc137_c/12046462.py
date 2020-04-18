import collections
N = int(input())

t = collections.defaultdict(int)
ans = 0

for _ in range(N):
    s = list(input())
    s.sort()
    t[''.join(s)] += 1


for x in t:
    ans += (t[x] * (t[x] - 1)) // 2

print(ans)

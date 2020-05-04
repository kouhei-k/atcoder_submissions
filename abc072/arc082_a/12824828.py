import collections
N = int(input())
a = list(map(int, input().split()))

c = collections.defaultdict(int)
ans = 0
for x in a:
    c[x] += 1
    c[x-1] += 1
    c[x+1] += 1
    ans = max(ans, c[x], c[x-1], c[x+1])

print(ans)

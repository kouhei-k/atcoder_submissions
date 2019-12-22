import collections
N = int(input())
a = list(map(int, input().split()))

table = collections.defaultdict(int)
m = 0
for i in range(N):
    table[a[i]] += 1
    if a[i] == m or a[i] == m+1:
        m = a[i]
if m == 0:
    print(-1)
else:
    print(N - m)

import collections
N = int(input())
A = [int(input()) for i in range(N)]
table = collections.defaultdict(int)
for x in A:
    table[x] += 1
ans = 0
for x in table:
    if table[x] > 1:
        ans += table[x] - 1
print(ans)

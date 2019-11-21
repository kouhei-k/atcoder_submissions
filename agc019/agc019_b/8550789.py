import collections
table = collections.defaultdict(int)
A = list(input())
N = len(A)

for x in A:
    table[x] += 1
ans = (N*(N-1) // 2) + 1
for x in table:
    ans -= (table[x] * (table[x] - 1)) // 2

print(ans)

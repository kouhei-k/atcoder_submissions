from itertools import combinations
import collections
N = int(input())
S = [input() for i in range(N)]
table = collections.defaultdict(int)

for x in S:
    table[x[0]] += 1

tmp = ["M", "A", "R", "C", "H"]


ans = 0
for x in combinations(tmp, 3):
    ans += table[x[0]]*table[x[1]]*table[x[2]]
print(ans)

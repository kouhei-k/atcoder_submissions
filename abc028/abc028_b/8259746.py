import collections
S = input()
table = collections.defaultdict(int)

for x in S:
    table[x] += 1
ans = []
for x in "ABCDEF":
    ans.append(str(table[x]))

print(" ".join(ans))

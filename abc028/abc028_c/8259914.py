import collections
ABCDE = list(map(int, input().split()))
ans = []
table = collections.defaultdict(int)
for i in ABCDE:
    for j in ABCDE:
        if i == j:
            continue
        for k in ABCDE:
            if i == k or j == k:
                continue
            table[i+j+k] += 1
ans = list(table.keys())
ans.sort()
print(ans[-3])

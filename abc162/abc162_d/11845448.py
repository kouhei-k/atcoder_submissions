import collections
import bisect
N = int(input())
S = input()
ans = 0
table = collections.defaultdict(list)
for i, x in enumerate(S):
    table[x].append(i)
R = len(table["R"])
G = len(table["G"])
L = len(table["B"])

s = set(table["B"])

for i in range(R):
    for j in range(G):
        x = table["R"][i]
        y = table["G"][j]
        if x > y:
            x, y = y, x
        ans += L
        if 2*y - x in s:
            ans -= 1
        if 2*x - y in s:
            ans -= 1
        if (x+y) % 2 == 0 and (x+y)//2 in s:
            ans -= 1

print(ans)

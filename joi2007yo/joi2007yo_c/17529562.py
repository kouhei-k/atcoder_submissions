alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = dict()
for i, x in enumerate(alpha):
    d[x] = i
S = input()
ans = []
for x in S:
    i = d[x]
    ans.append(alpha[(i-3) % 26])
print("".join(ans))

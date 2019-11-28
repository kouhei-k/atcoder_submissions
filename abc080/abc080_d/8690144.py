import collections
N, C = map(int, input().split())
stc = [list(map(int, input().split())) for i in range(N)]

stc.sort(key=lambda x: x[0])
table = collections.defaultdict(list)
for s, t, c in stc:
    table[c].append((s, t))
maxtime = 0
for x in table:
    for i in range(len(table[x]) - 1):
        if table[x][i][1] == table[x][i+1][0]:
            table[x][i+1] = (table[x][i][0], table[x][i+1][1])
            table[x][i] = (-1, -1)
    maxtime = max(maxtime, table[x][-1][1])

im = [0]*(maxtime+2)

for x in table:

    for s, t in table[x]:
        if s == -1:
            continue
        im[s] += 1
        im[t+1] -= 1

s = [0]*(maxtime+3)
for i in range(1, maxtime+2):
    s[i+1] = s[i]+im[i]

print(max(s))

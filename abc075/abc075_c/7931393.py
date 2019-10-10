import collections
N, M = map(int, input().split())
a = [0]*M
b = [0]*M
table = collections.defaultdict(list)
for i in range(M):
    a[i], b[i] = map(int, input().split())
    table[a[i]].append(b[i])
    table[b[i]].append(a[i])
bridge = []
for x in table:
    if len(table[x]) < 2:
        bridge.append(x)
prev = 0
now = len(bridge)
while(prev != now):
    for x in table:
        if x not in bridge:
            lenx = len(table[x])
            for y in table[x]:
                if y in bridge:
                    lenx -= 1
            if lenx < 2:
                bridge.append(x)
    prev = now
    now = len(bridge)
ans = 0
for i in range(M):
    if a[i] in bridge or b[i] in bridge:
        ans += 1

print(ans)

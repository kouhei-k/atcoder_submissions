import collections
N, M = map(int, input().split())
X = list(map(int, input().split()))

table = collections.defaultdict(list)
for x in X:
    table[x % M].append(x)
Count = [None]*M
for i in range(M):
    Count[i] = collections.Counter(table[i]).values()
ans = 0
for i in range(M // 2 + 1):
    tmp = min(len(table[i]), len(table[(M-i) % M]))
    if i != (M-i) % M:
        ans += tmp
    else:
        ans += tmp // 2

    k = 0
    l = 0
    for x in Count[i]:
        k += x % 2
        l += x // 2
    if tmp <= k:
        ans += l
    else:
        ans += ((k + l*2) - tmp) // 2

    if i != (M-i) % M:
        k = 0
        l = 0
        for x in Count[(M-i) % M]:
            k += x % 2
            l += x // 2
        if tmp <= k:
            ans += l
        else:
            ans += ((k + l*2) - tmp) // 2

print(ans)

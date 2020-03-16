import collections
S = [input() for i in range(3)]
N = len(S[0]) // 2
t = collections.defaultdict(int)
t2 = collections.defaultdict(int)
t3 = collections.defaultdict(int)
for x in S[0]:
    t[x] += 1
for x in S[1]:
    t2[x] += 1
for x in S[2]:
    t3[x] += 1

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d = dict()
for i, x in enumerate(alpha):
    d[x] = 0

c0 = 0
c1 = 0
for x in t3:
    if x not in t2 and x in t:
        if t[x] >= t3[x]:
            c0 += t3[x]
        else:
            print("NO")
            exit(0)
    elif x not in t and x in t2:
        if t2[x] >= t3[x]:
            c1 += t3[x]
        else:
            print("NO")
            exit(0)

    elif x not in t and x not in t2:
        print("NO")
        exit(0)
    else:
        if t[x] + t2[x] < t3[x]:
            print("NO")
            exit(0)

        if t[x] < t3[x]:
            c1 += t3[x] - t[x]
            t2[x] -= t3[x] - t[x]
            t3[x] = t[x]
        if t2[x] < t3[x]:
            c0 += t3[x] - t2[x]
            t[x] -= t3[x] - t2[x]
            t3[x] = t2[x]
        if t3[x] > 0:
            d[x] = t3[x]


if c0 > N or c1 > N:
    print("NO")
    exit(0)
for x in t3:
    if t3[x] > 0:
        c0 += min(t3[x], t[x])
        c1 += min(t3[x], t2[x])
if c0 < N or c1 < N:
    print("NO")
    exit(0)

print("YES")

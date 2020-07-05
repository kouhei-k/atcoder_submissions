N = int(input())
S = [input() for i in range(N)]

key = ["AC", "WA", "TLE", "RE"]
d = dict()
for x in key:
    d[x] = 0
for x in S:
    d[x] += 1

for x in key:
    print(x, "x", d[x])

import bisect
X, N = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
s = set([i for i in range(102)])

for x in p:
    s.remove(x)

s = sorted(list(s))

id = bisect.bisect_left(s, X)
a = s[id-1]
b = s[id]
ans = a
if abs(a-X) > abs(b-X):
    print(b)
else:
    print(a)

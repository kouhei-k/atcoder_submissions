import collections
N = int(input())
A = list(map(int, input().split()))


ans = 0
t = collections.defaultdict(int)
t2 = collections.defaultdict(int)
for i, x in enumerate(A):
    t[i-x] += 1
    t2[x+i] += 1
for i, x in enumerate(A):
    ans += t[x+i]
    ans += t2[i-x]

print(ans // 2)

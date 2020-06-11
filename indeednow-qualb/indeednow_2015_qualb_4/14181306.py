import collections
N, C = map(int, input().split())
a = list(map(int, input().split()))


d = collections.defaultdict(list)
for i, x in enumerate(a):
    d[x].append(i)

for i in range(1, C+1):
    if i not in d:
        print(0)
    else:
        ans = N*(N+1) // 2
        L = len(d[i])
        left = 0
        for x in d[i]:
            k = x - left
            ans -= k*(k+1)//2
            left = x+1
        if d[i][-1] != N-1:
            k = N - left
            ans -= k*(k+1)//2
        print(ans)

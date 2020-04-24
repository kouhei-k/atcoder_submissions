import collections
N = int(input())
A = list(map(int, input().split()))
t = collections.defaultdict(int)
for x in A:
    t[x] += 1
ans = 0
for x in t:
    ans += t[x]*(t[x]-1) // 2
for x in A:
    tmp = ans
    tmp -= (t[x]*(t[x] - 1)) // 2
    print(tmp + ((t[x]-1)*(t[x]-2))//2)

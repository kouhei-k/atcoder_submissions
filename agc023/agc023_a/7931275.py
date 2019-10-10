import collections
N = int(input())
A = list(map(int, input().split()))

sumA = [0]*(N+1)
table = collections.defaultdict(int)
table[0] += 1
for i in range(N):
    sumA[i+1] = sumA[i]+A[i]
    table[sumA[i+1]] += 1
ans = 0
table = table.values()
table = [x for x in table if x > 1]
for x in table:
    ans += x*(x-1)//2

print(ans)

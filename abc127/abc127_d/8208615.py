import collections
import bisect
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [0]*M
C = [0]*M
table = collections.defaultdict(int)
for x in A:
    table[x] += 1
for i in range(M):
    B[i], C[i] = map(int, input().split())
    table[C[i]] += B[i]

count = N
ans = 0
table = list(table.items())
table.sort(key=lambda x: x[0], reverse=True)
for x in table:
    if count > x[1]:
        count -= x[1]
        ans += x[0]*x[1]
    else:
        ans += x[0]*count
        break

print(ans)

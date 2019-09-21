N, M = map(int, input().split())
A = list(map(int, input().split()))
import collections
mod_table=collections.defaultdict(int)
com_sum = [0] * (N+1)
for i in range(N):
    com_sum[i+1] = A[i] + com_sum[i]
ans = 0
for i in range(N+1):
    mod = com_sum[i] % M
    mod_table[mod]+=1
    
for x in mod_table:
  y = mod_table[x]
  if y > 1:
    ans += y*(y-1)//2

print(ans)

N=int(input())
A=[int(input()) for i in range(N)]
A.sort()
mod=10**9 + 7
s=[0]*(N+1)
for i in range(N):
  s[i+1]=s[i]+A[i]
print(sum(s))

import collections
table=collections.defaultdict(int)
for x in A:
  table[x]+=1
import math
ans=1
for x in table:
  ans*=math.factorial(table[x])%mod
print(ans%mod)

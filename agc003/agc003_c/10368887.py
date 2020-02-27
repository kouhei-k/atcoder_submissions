N=int(input())
A=[int(input()) for i in range(N)]
odd =[A[i] for i in range(N) if i%2 ==0]
even=[A[i] for i in range(N) if i%2 ==1]
import collections
table=collections.defaultdict(int)
table2=collections.defaultdict(int)
A.sort()
for i in range(N):
  if i %2==0:
    table[A[i]]+=1
for x in odd:
  table2[x]+=1
ans=0

for x in table:
  ans+=(table[x] -table2[x])

print(ans)

N,T=map(int,input().split())
A=list(map(int,input().split()))


import heapq
import collections
hq=[]
heapq.heapify(hq)
heapq.heappush(hq,A[0])
tmp=0
table=collections.defaultdict(int)
for i in range(1,N):
  j=heapq.heappop(hq)
  table[A[i]-j]+=1
  tmp=max(tmp,A[i]-j)
  heapq.heappush(hq,j)
  heapq.heappush(hq,A[i])
print(table[tmp])

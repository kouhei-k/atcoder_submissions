X,Y,Z,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A.sort()
B.sort()
C.sort()
AB=[]
for a in A:
  for b in B:
    AB.append(-(a+b))
import heapq
heapq.heapify(AB)
ABC=[]
for _ in range(min(K,len(AB))):
  ab=heapq.heappop(AB)
  for c in C:
    heapq.heappush(ABC,ab-c)
for i in range(K):
  print(-heapq.heappop(ABC))
  

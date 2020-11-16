N,K=map(int,input().split())
import heapq
AB=[tuple(map(int,input().split())) for i in range(N)]
heapq.heapify(AB)
ans=0
for _ in range(K):
  a,b=heapq.heappop(AB)
  ans+=a
  a+=b
  heapq.heappush(AB,(a,b))
print(ans)

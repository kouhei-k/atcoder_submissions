N,K=map(int,input().split())
X=list(map(int,input().split()))
#i位以上の人でK番目に若い人
import heapq
hq=[(-X[i],i) for i in range(K)]
heapq.heapify(hq)

#K番目の人より大きかったら変化なし
#逆なら
print(hq[0][1]+1)
for i in range(K,N):
  heapq.heappush(hq,(-X[i],i))
  heapq.heappop(hq)
  print(hq[0][1]+1)

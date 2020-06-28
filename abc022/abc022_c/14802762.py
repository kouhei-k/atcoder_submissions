import heapq
N,M=map(int,input().split())

G=[set() for i in range(N)]
for i in range(M):
  u,v,l =map(int,input().split())
  u-=1
  v-=1
  G[u].add((v,l))
  G[v].add((u,l))


ans=10**9
for i,cost in G[0]: 
    hq=[(0,i,0)]
    d=[-1]*N
    d[i]=0
    while(hq):
      c,x,y=heapq.heappop(hq)
     
      if x==0:
        ans=min(ans,c+cost)
        break
        
      for z,cz in G[x]:
        if z==x or z==y:
          continue
        if d[z]<0 or c+cz < d[z]:
          d[z] = c+cz
          heapq.heappush(hq,(d[z],z,x))
    
if ans==10**9:
  ans=-1
print(ans)

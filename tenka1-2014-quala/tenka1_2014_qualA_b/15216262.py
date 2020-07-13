S=input()
k=5
import heapq
hq = []
hq2=[]
combo=0
ans=0
charging=0
for i,x in enumerate(S):
  charging-=1
  if charging>0:
    continue
  if x == "-":
    continue
  else:
    while(hq and hq[0][0]<i):
      k+=hq[0][1]
      heapq.heappop(hq)
    while(hq2 and hq2[0]<i):
      combo+=1
      heapq.heappop(hq2)
    if k>0 and x=="N":
      heapq.heappush(hq,(i+6,1))
      heapq.heappush(hq2,i+1)
      ans+=10*(1+(combo//10 *0.1))
      k-=1
    elif k>2 and x =="C":
      heapq.heappush(hq,(i+8,3))
      heapq.heappush(hq2,i+3)
      ans+=50*(1+(combo//10 * 0.1))
      charging=2.5
      k-=3

print(int(ans))

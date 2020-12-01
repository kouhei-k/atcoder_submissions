R,C,K=map(int,input().split())
N=int(input())
RD=dict()
CD=dict()
RR=dict()
CC=dict()
CC[0]=0
CC[K]=0


for i in range(N):
  r,c=map(int,input().split())
  r-=1
  c-=1

  if r in RD:
    RD[r].add(c)
  else:
    RD[r]=set([c])
  if c in CD:
    CD[c].add(r)
  else:
    CD[c]=set([r])
        
for x in RD:
  l = len(RD[x])
  if l in RR:
    RR[l]+=1
  else:
    RR[l]=1
for x in range(C):
  if x not in CD:
    CC[0]+=1
    continue
    
  l=len(CD[x])
  if l in CC:
    CC[l]+=1
  else:
    CC[l]=1
ans=0
for i in range(R):
  if i not in RD:
    ans+=CC[K]
    continue
 
  x=len(RD[i])
  if x>K:
    continue
  if K-x in CC:
    ans+=CC[K-x]
  for c in RD[i]:

    if len(CD[c])==K-x:
      ans-=1
    elif len(CD[c])==K-x+1:
      ans+=1
print(ans)

N=int(input())
S=[tuple(map(int,list(input()))) for i in range(N)]
G=[set() for i in range(N)]
for i in range(N):
  for j in range(N):
    if S[i][j]==1:
      G[i].add(j)

S=set()
X=[]
Y=[]
import collections
q=collections.deque()
for i in range(N):

  if i in S:
    continue
  A=set()
  B=set()
  A.add(i)
  q.append(i)
  while(q):
    x=q.popleft()
    for y in G[x]:
      if y in A:
        if x in A:
          print(-1)
          exit(0)
        else:
          continue
      elif y in B:
        if x in B:
          print(-1)
          exit(0)
        else:
          continue
      else:
        if x in A:
          B.add(y)
        else:
          A.add(y)
        q.append(y)
  S|=A
  S|=B
  X.append(A)
  Y.append(B)
ans=1
for x, y in zip(X,Y):
  tmp=1
  for i in x|y:
    q.append((i,1))
    s=set()
    s.add(i)
    
    while(q):
      a,c=q.popleft()
      if c>tmp:
        tmp=c
      for b in G[a]:
        if b in s:
          continue
        else:
          s.add(b)
          q.append((b,c+1))
  ans+=tmp-1
print(ans)

                
          
        

      
               
  
 
      
    
  

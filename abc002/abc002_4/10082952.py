N,M=map(int,input().split())
G=[set([i]) for i in range(N)]
for i in range(M):
  a,b=map(int,input().split())
  a-=1
  b-=1
  G[a].add(b)
  G[b].add(a)
ans=0
for i in range(2**N):
  tmp=set()
  for j in range(N):
    if (i>>j)%2==1:
      tmp.add(j)
  flag=True
  for x in tmp:
    if tmp & G[x]== tmp:
      continue
    else:
      flag=False
      break
  if flag:
    ans=max(len(tmp),ans)
print(ans)
      

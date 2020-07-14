N,K=map(int,input().split())
AB=[tuple(map(int,input().split())) for i in range(N)]
AB.sort(key=lambda x:x[1])
prev=[AB[-1][0],AB[-1][1]*AB[-1][0]/100]
s=set([N-1])
id=-1
for _ in range(K-1):
  next=[1,-1]
  for i in range(N):
    if i in s:
      continue
    W,w=AB[i]
    w*=W / 100
    if next[1]/next[0] < (prev[1]+w)/(prev[0]+W):
      id=i
      next[0]=prev[0]+W
      next[1]=prev[1]+w
  s.add(id)
  prev[0]=next[0]
  prev[1]=next[1]
print(prev[1]/prev[0]*100)
#print(s,prev)

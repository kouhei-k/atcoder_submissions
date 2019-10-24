N=int(input())
a=list(map(int,input().split()))
ans=0
maxscore=[-2500]*N
for i in range(N):
  score=[[0,0] for j in range(N)]
  for j in range(N):
    if i == j:
      score[i]=[-2500,-2500]
      continue
    s,t=min(i,j),max(i,j)
    l = a[s:t+1]
    for k in range(t-s+1):
      if k%2==0:
        score[j][1]+=l[k]
      else:
        score[j][0]+=l[k]
        
  score.sort(reverse=True, key=lambda x:x[0])
  maxscore[i]=score[0][1]
print(max(maxscore))
      
      

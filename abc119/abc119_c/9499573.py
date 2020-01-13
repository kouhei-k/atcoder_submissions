N,A,B,C=map(int,input().split())
l=[int(input()) for i in range(N)]
ans=10**9
for i in range(4**N):
  tmp=[0]*N
  s=[0,0,0]
  for j in range(N):
    k = (i // (4**j))%4
    tmp[j]=k
    if k>0:
      s[k-1]+=1
  if s[0]==0 or s[1]==0 or s[2]==0:
    continue
  else:
    ans_tmp=0
    ans_tmp=10*(max(s[0]-1,0)+max(s[1]-1,0) +max(s[2]-1,0))
    s[0],s[1],s[2]=0,0,0
    for j in range(N):
      if tmp[j]==0:
        continue
      s[tmp[j]-1]+=l[j]
    ans_tmp+=abs(s[0]-A)+abs(s[1]-B)+abs(s[2]-C)
    ans=min(ans,ans_tmp)
print(ans)
    
    

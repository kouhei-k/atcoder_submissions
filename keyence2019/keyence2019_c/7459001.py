N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

diff=[[A[i]-B[i],i] for i in range(N)]
diff=sorted(diff,key=lambda x:x[0])

idx=-1
for i in range(N):
  while(diff[i][0]<0):
    if diff[idx][0]< 0:
      print("-1")
      exit(0)
    if abs(diff[i][0]) >= diff[idx][0]:
      diff[i][0]+=diff[idx][0]
      diff[idx][0]=0
      idx-=1
    else:
      diff[idx][0]+=diff[i][0]
      diff[i][0]=0
diff=sorted(diff,key=lambda x:x[1])
C=[B[i]+diff[i][0] for i in range(N)]
ans=0
for i in range(N):
  if A[i]!=C[i]:
    ans+=1
print(ans)

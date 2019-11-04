N=int(input())
a=list(map(int,input().split()))
if sum(a)%N!=0:
  print(-1)
else:
  t= sum(a)//N
  diff = [t-a[i] for i in range(N)]
  s=[0]*N
  s[0]=diff[0]
  for i in range(1,N):
    s[i]=diff[i]+s[i-1]
  id=0
  ans=0
  for i in range(N):
    if s[i] == 0:
      ans+=i-id
      id = i+1
  print(ans)
    
    

N,S,T=map(int,input().split())
W=int(input())
ans=0
if W>=S and W<=T:
  ans=1
else:
  ans=0
for i in range(1,N):
  W+=int(input())
  if W>=S and W<=T:
    ans+=1
print(ans)

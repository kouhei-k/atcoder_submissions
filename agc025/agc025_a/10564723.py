N=list(input())
ans=0
for x in N:
  x=int(x)
  if x%2==1:
    ans+=1
  ans+=(x//2)*2
if ans==1:
  print(10)
else:
  print(ans)

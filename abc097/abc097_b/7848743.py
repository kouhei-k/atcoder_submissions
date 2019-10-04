X=int(input())
ans=0
for i in range(2,10):
  tmp=int(pow(X,1/i)+1)**i
  if tmp > X:
    tmp=int(pow(X,1/i))**i
  ans=max(ans,tmp)
print(ans)

n=int(input())
ans=n
for i in range(1,n+1):
  tmp=abs(n//i - i) +n%i
  ans=min(ans,tmp)
print(ans)
  

N=int(input())
K=int(input())

ans=2**N

for i in range(2**N):
  tmp=1
  for j in range(N):
    if (i>>j) %2==1:
      tmp*=2
    else:
      tmp+=K     
  ans=min(ans,tmp)
print(ans)

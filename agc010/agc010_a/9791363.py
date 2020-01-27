N=int(input())
A=list(map(int,input().split()))
count=0
for i in range(N):
  if A[i]%2==1:
    count+=1

ans=["YES","NO"]

print(ans[count%2])
    
    
    
    

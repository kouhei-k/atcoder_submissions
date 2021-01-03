ans=0
N=int(input())
A=list(map(int,input().split()))
count=0
for i in range(N):
  if A[i]==1:
    count+=1
  else:
    count=0
  if count>ans:
    ans=count
print(ans+1)

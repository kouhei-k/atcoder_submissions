N=int(input())
a=list(map(int,input().split()))


diff=[a[i]-a[i-1] for i in range(1,N)]
count=1
ans=0
for i in range(N):
  if i != N-1:
    if diff[i]>0:
      count+=1
      continue
  ans+=count*(count+1)//2
  count=1
  
print(ans)

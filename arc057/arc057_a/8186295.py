A,K=map(int,input().split())
target=2*10**12
count=0
if K>0:
  while(A<target):
    count+=1
    A+=1+K*A
  print(count)
else:
  print(target-A)

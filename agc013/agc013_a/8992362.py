N=int(input())
a=list(map(int,input().split()))
flag=0
ans=1
for i in range(1,N):
  if flag== 0:
    if a[i]>a[i-1]:
      flag=1
      continue
    elif a[i]<a[i-1]:
      flag=-1
      continue
    else:
      continue
  elif flag>0:
    if a[i]<a[i-1]:
      ans+=1
      flag=0
  else:
    if a[i]>a[i-1]:
      ans+=1
      flag=0
print(ans)    

    

N=int(input())
A=list(map(int,input().split()))
A.sort()
B=[A[i] for i in reversed(range(N)) if A[i]<0]
C=[A[i] for i in range(N) if A[i]>=0]
s=0
if len(B)>0 and len(C)>0:
  s=sum(B)*-1
  s+=sum(C)
else:
  if len(B)>0:
    s=B[0]-(sum(B)-B[0])
  else:
    s=sum(C)-C[0]*2
print(s)
tmp=0
if len(B)==0:
  tmp=C[0]
  for i in range(2,len(C)):
    print(tmp,C[i])
    tmp-=C[i]
  print(C[1],tmp)
  
  
elif len(C)==0:
  tmp=B[0]
  for i in range(1,len(B)):
    print(tmp,B[i])
    tmp-=B[i]
else:
  tmp=C[0]
  tmp2=B[0]
  for i in range(1,len(B)):
    print(tmp,B[i])
    tmp-=B[i]
  for i in range(1,len(C)):
    print(tmp2,C[i])
    tmp2-=C[i]
  print(tmp,tmp2)
  tmp-=tmp2

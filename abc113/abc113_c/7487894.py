N,M=map(int,input().split())
PY=[[0,0,0] for i in range(M)] 
for i in range(M):
  P,Y=map(int,input().split())
  PY[i]=[P,Y,i]
PY.sort(key=lambda x:x[1])
PY.sort(key=lambda x:x[0])
prev=0
for i in range(M):
  if PY[i][0] != prev:
    count = 1
  else:
    count+=1
  prev=PY[i][0]
  ans=["0" for i in range(6 - len(str(prev)))]
  temp=["0" for i in range(6 - len(str(count)))]
  ans+=list(str(prev))+temp+list(str(count))
  PY[i][0]="".join(ans)
PY.sort(key=lambda x:x[2])
for i in range(M):
  print(PY[i][0])

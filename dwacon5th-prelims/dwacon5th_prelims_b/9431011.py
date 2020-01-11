import bisect
import copy
N,K=map(int,input().split())
a=list(map(int,input().split()))
s=[0]*(N+1)
for i in range(N):
  s[i+1]=s[i]+a[i]
sumList=[]
for i in range(N):
  for j in range(i,N):
    tmp=s[j+1]-s[i]
    sumList.append(tmp)
sumList.sort()
#print(sumList)
tmp=len(bin(sumList[-1]))-2+1
tmp=2**tmp
ans=0
while(tmp != 0):
  #print(tmp)
  tmpList=[sumList[i] % tmp for i in range(len(sumList)) if sumList[i]%tmp>=(tmp//2)]
  #print(tmpList)
  if len(tmpList)>=K:
    ans+=tmp//2
    #print(tmp//2)
    sumList=copy.copy(tmpList)
  tmp = tmp // 2
  
print(ans)



    

N,K=map(int,input().split())
ab=[[0]*2 for i in range(N)]
for i in range(N):
  ab[i]=list(map(int,input().split()))
  
ab=sorted(ab,key=lambda x:x[0])
i=-1
while(K > 0):
  i+=1
  K -= ab[i][1]

print(ab[i][0])

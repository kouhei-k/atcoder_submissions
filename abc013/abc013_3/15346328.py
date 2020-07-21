import math
N,H=map(int,input().split())
A,B,C,D,E=map(int,input().split())
ans=10**15
hungry=N*E-H
B+=E
D+=E
for i in range(N+1):
  k = hungry - B*i
  j = max(math.ceil((k+1)/D),0)
  ans=min(A*i+C*j,ans)
  
print(ans)

import math
Q = int(input())

def sosuu(x):
  if x == 1:
    return False
  else:
    for i in range(1,int(math.sqrt(x))):
      if x % (i+1) == 0:
        return False
    return True

table=[0]*50001
for i in range(1,50001):
  if sosuu(2*i - 1) and sosuu(i):
    table[i]=table[i-1] + 1
  else:
    table[i]=table[i-1]
    
ans=[0]*Q
for i in range(Q):
  l,r=map(int,input().split())
  ans[i]=table[(r+1)//2] - table[(l+1)//2 - 1]
  
for i in range(Q):
  print(ans[i])
  

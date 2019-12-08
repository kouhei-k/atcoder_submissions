import math
N=int(input())
t =[0]*5
for i in range(5):
  t[i]=int(input())
  
min_t = min(t)
ans= math.ceil(N / min_t) + 4
print(ans)

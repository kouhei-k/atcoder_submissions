N=int(input())
xy=[list(map(int,input().split())) for i in range(N)]
from itertools import combinations
ans=0
for a,b,c in combinations(xy,3):
  S=abs((b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1]))
 # print(S,a,b,c) 
  if S!=0 and S%2==0:
    ans+=1
print(ans)

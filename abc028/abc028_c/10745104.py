from itertools import combinations
a=list(map(int,input().split()))
ans=[]
for x in combinations(a,3):
  ans.append(sum(x))
print(sorted(ans)[-3])

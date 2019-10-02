import collections
N=int(input())
S =input()
def countchar(s1,s2):
  ret=0
  table=collections.defaultdict(int)
  for x in s1:
    table[x]+=1
  for x in s2:
    if x in table and table[x]>0:
      ret+=1
      table[x]=0
  return(ret)
ans=0
for i in range(1,N):
  X=S[:i]
  Y=S[i:]
  ans=max(ans,countchar(X,Y))
print(ans)

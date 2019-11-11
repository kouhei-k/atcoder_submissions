N=int(input())
c=input()
commands=["A","B","X","Y"]
macro=[]
for x in commands:
  for y in commands:
    macro.append(x+y)
ans=N
for L in macro:
  for R in macro:
    if L==R:
      continue
    id=0
    tmp=0
    while(id<N):
      if id <N-1 and (c[id]+c[id+1]==L or c[id]+c[id+1]==R):
        id+=2
      else:
        id+=1
      tmp+=1
    ans=min(tmp,ans)
print(ans)
      

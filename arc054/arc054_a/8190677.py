L,X,Y,S,D=map(int,input().split())
ans=[0,float("Inf")]
if D>=S:
  ans[0]=(D-S)/(X+Y)
  if Y>X:
    ans[1]=(S+L-D)/(Y-X)
else:
  ans[0]=(L-S +D )/(X+Y)
  if Y>X:
    ans[1]=(S-D)/(Y-X)
  
print(min(ans))

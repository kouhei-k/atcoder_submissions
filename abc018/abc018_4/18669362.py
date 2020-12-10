N,M,P,Q,R=map(int,input().split())


D=[set() for i in range(N)]
for i in range(R):
  x,y,z = map(int,input().split())
  x-=1
  y-=1
  D[x].add((y,z))
ans=0
for i in range(2**P - 1, 2**N):
  A=set()
  for j in range(N):
    if (i>>j)%2==1:
      A.add(j)
  if len(A)!=P:
    continue
  B=[0]*M
  for x in A:
    for y,z in D[x]:
      
      B[y]+=z
  B.sort(reverse=True)
  if ans< sum(B[:Q]):
    ans=sum(B[:Q])
print(ans)

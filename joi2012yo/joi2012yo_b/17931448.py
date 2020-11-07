N=int(input())
point=[0]*N
for i in range(N*(N-1)//2):
  a,b,c,d=map(int,input().split())
  a-=1
  b-=1
  if c>d:
    point[a]+=3
  elif c<d:
    point[b]+=3

  else:
    point[a]+=1
    point[b]+=1
A=[(point[i],i) for i in range(N)]
A.sort(reverse=True)
prev=N*N

ans=0
order=[0]*N
for i in range(N):
  x,y=A[i]
  if x < prev:
    prev=x
    ans=i+1
  order[y]=ans
print(*order, sep='
')

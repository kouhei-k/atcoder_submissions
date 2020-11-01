N=int(input())
K=int(input())
for i in range(K):
  x,y=map(int,input().split())
  x=min(x,y,N-x+1,N-y+1)
  x%=3
  if x==0:
    x=3
  print(x)
  

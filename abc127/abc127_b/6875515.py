r,D,x=map(int,input().split())
prev=x
for _ in range(10):
  prev=r*prev -D
  print(prev)

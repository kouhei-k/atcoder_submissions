N,M,X,Y=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))

x=sorted(x)
y=sorted(y)

if x[-1] < y[0] and X < y[0] and x[-1] < Y:
  print("No War")
else:
  print("War")
  
  

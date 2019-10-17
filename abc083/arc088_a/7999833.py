X,Y=map(int,input().split())
d=Y-X
k= Y // X
if k <= 1:
  print(1)
  exit(0)
count=1
while(1):
  if k < 2**count:
    break
  elif k ==2**count:
    count+=1
    break
  else:
    count+=1
print(count)

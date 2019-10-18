x=int(input())
k=x%11
if k == 0:
  print((x//11)*2)
elif k <= 6:
  print((x//11)*2+1)
else:
  print((x//11)*2+2)

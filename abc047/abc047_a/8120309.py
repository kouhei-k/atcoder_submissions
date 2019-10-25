abc=list(map(int,input().split()))
abc.sort()
if sum(abc[:2]) ==abc[2]:
  print("Yes")
else:
  print("No")

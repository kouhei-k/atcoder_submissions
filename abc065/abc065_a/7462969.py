X,A,B=map(int,input().split())
if B - A > X:
  print("dangerous")
else:
  if B <= A:
    print("delicious")
  else:
    print("safe")

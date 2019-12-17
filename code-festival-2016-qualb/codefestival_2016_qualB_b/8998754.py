N,A,B=map(int,input().split())
dom=0
foreign=0
for x in input():
  if x == "a":
    if dom+foreign<A+B:
      dom+=1
      print("Yes")
    else:
      print("No")
  elif x == "b":
    if dom+foreign<A+B and foreign<B:
      foreign+=1
      print("Yes")
    else:
      print("No")
  else:
    print("No")

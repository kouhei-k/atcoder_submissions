X=list(input())
while(len(X) >0):
  if len(X)>=2 and X[-2]+X[-1]=="ch":
    X.pop()
    X.pop()
    continue
  elif X[-1]=="o" or X[-1]=="k" or X[-1]=="u":
    X.pop()
    continue
  else:
    print("NO")
    exit(0)
print("YES")

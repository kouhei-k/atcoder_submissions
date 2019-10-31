N=int(input())
for i in range(3**N):
  ans=[]
  for j in range(N):
    k=i//(3**j)
    if k%3==0:
      ans.append("a")
    elif k%3==1:
      ans.append("b")
    else:
      ans.append("c")
  print("".join(list(reversed(ans))))
  

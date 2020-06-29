import collections
N=int(input())
D=collections.Counter("indeednow")
for i in range(N):
  S=input()
  if len(S)!=9:
    print("NO")
    continue
  C=collections.Counter(S)
  flag=True
  for x in "indeednow":
    if x in C:
      if C[x]!=D[x]:
        print("NO")
        flag=False
        break
    else:
      print("NO")
      break
   
  if flag:
    print("YES")
  

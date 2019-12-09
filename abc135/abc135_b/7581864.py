N=int(input())
p=list(map(int,input().split()))
foundpair=False
foundi=False
sortedp=sorted(p)
pair=[]
if p==sortedp:
  print("YES")
  exit(0)
for i in range(N):
  if p[i]== sortedp[i]:
    continue
  else:
    if foundpair==False:
      if foundi:
        foundpair=True
        pair.append(i)
      else:
        foundi=True
        pair.append(i)
    else:
      print("NO")
      exit(0)
      
p[pair[0]],p[pair[1]]=p[pair[1]],p[pair[0]]
if p==sortedp:
  print("YES")
else:
  print("NO")
      

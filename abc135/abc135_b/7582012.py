N=int(input())
p=list(map(int,input().split()))
count=0
pair=[]
for i in range(N):
  if p[i]== i+1:
    continue
  else:
    if count<2:
      count+=1
      pair.append(i)
    else:
      print("NO")
      exit(0)
      
print("YES")
      

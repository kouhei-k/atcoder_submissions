ab=[tuple(map(int,input().split())) for i in range(3)]
count=[0,0,0,0]
for a,b in ab:
  count[a-1]+=1
  count[b-1]+=1
if max(count)>=3:
  print("NO")
else:
  print("YES")

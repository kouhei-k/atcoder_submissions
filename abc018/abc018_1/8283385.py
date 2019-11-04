abc=[[int(input()),i] for i in range(3)]
abc.sort(reverse=True)
ans=[0,0,0]
for i in range(3):
  ans[abc[i][1]]=i+1
for i in range(3):
  print(ans[i])

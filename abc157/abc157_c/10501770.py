N,M=map(int,input().split())
d = dict()
for i in range(M):
  a,b=map(int,input().split())
  if a not in d:
    d[a]=b
  else:
    if d[a]!=b:
      print(-1)
      exit(0)
tmp=0
for i in range(10):
  if 3 in d and d[3] != i:
    continue
  for j in range(10):
    if 2 in d and d[2] != j:
      continue
    for k in range(10):
      if N!=1 and k ==0:
        continue
      if 1 in d and d[1]!= k:
        continue
      print((str(k)+str(j)+str(i))[:N])
      exit(0)
print(-1)

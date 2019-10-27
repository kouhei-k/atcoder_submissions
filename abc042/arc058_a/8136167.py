N,K=map(int,input().split())
D=list(input().split())

for i in range(N,10*N+1):
  s=str(i)
  flag=True
  for x in D:
    if x in s:
      flag=False
      break
  if flag:
    print(s)
    break
  else:
    continue

    

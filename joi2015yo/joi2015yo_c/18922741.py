H,W=map(int,input().split())
for _ in range(H):
  c=input()
  ans=[]
  A=-1
  for i, x in enumerate(c):
    if x == 'c':
      A=i
      ans.append(0)
    else:
      if A<0:
        ans.append(-1)
      else:
        ans.append(i-A)
  print(' '.join(map(str,ans)))
      
      
      
  

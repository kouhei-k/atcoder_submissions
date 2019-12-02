g=[list(input()) for i in range(10)]
import collections
num=0
for i in range(10):
  for j in range(10):
    if g[i][j]=="o":
      num+=1

for i in range(10):
  for j in range(10):
    if g[i][j]=="o":
      continue
    else:
      q=collections.deque()
      q.append([i,j])
      tmp=0
      gtmp=[[True]*10 for i in range(10)]
      gtmp[i][j]=False
      while(q):
        tmp+=1
  
        k,l=q.popleft()

        if k >0:
          if g[k-1][l]=="o" and gtmp[k-1][l]:
            q.append([k-1,l])
            gtmp[k-1][l]=False
        if k<9:
          if g[k+1][l]=="o" and gtmp[k+1][l]:
            q.append([k+1,l])
            gtmp[k+1][l]=False
        if l>0:
          if g[k][l-1]=="o" and gtmp[k][l-1]:
            q.append([k,l-1])
            gtmp[k][l-1]=False
        if l<9:
          if g[k][l+1]=="o" and gtmp[k][l+1]:
            q.append([k,l+1])
            gtmp[k][l+1]=False
      if tmp == num+1:
        print("YES")
        exit(0)
print("NO")

h,w=map(int,input().split())
import collections
D=[[0]*(w+2) for i in range(h+2)]
D[0][1]=1
D2=[[0]*(w+2) for i in range(h+2)]
D2[1][0]=1
#曲がったかどうか考慮する必要
for i in range(h):
  for j in range(w):
    if i ==j==0:
      continue
    else:
      D[i][j+1]+=D[i][j]
      D2[i+2][j]+=D[i][j]
      D[i][j+2]+=D2[i][j]
      D2[i+1][j]+=D2[i][j]
      if i+1==h-1 and j==w-1:
        D2[i+1][j]+=D[i][j]
      elif i==h-1 and j+1==w-1:
        D[i][j+1]+=D2[i][j]
mod=10**5
print((D[h-1][w-1]+D2[h-1][w-1])%mod)

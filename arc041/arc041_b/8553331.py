N,M=map(int,input().split())
field=[list(map(int,list(input()))) for i in range(N)]
ans=[[0]*M for i in range(N)]

for i in range(1,N-1):
  for j in range(1,M-1):
    
    while(field[i][j-1] >= 1 and field[i-1][j]>=1 and field[i][j+1]>=1  and field[i+1][j]>=1):
      field[i][j-1]-=1
      field[i][j+1]-=1
      field[i-1][j]-=1
      field[i+1][j]-=1
      ans[i][j]+=1
for i in range(N):
  print("".join(map(str,ans[i])))

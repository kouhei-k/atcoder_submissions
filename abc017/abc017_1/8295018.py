ans=0
se=[list(map(int,input().split())) for i in range(3)]
for i in range(3):
  ans+=int(se[i][0]*se[i][1]*0.1)
print(ans)

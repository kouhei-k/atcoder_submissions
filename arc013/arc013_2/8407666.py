C=int(input())
item=[list(map(int,input().split())) for i in range(C)]
for i in range(C):
  item[i].sort(reverse=True)

ans=[0,0,0]
for i in range(3):
  item.sort(key=lambda x:x[i])
  ans[i]=item[-1][i]
print(ans[0]*ans[1]*ans[2])

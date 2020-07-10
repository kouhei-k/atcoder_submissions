N,H,W=map(int,input().split())
ans=0
for i in range(N):
  x,y=map(int,input().split())
  if x>=H and y>=W:
    ans+=1
print(ans)

N=int(input())
w=list(input().split())
tmp=["TAKAHASHIKUN","Takahashikun","takahashikun"]
w[-1]=w[-1][:-1]
ans=0
for x in w:
  if x in tmp:
    ans+=1
print(ans)

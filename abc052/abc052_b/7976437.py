N=int(input())
S=input()
x=0
ans=0
for y in S:
  if y=="I":
    x+=1
    ans=max(x,ans)
  else:
    x-=1
print(ans)

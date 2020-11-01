S=input()
N=int(input())
ans=0
for i in range(N):
  x=input()
  x+=x[:-1]
  if S in x:
    ans+=1
print(ans)

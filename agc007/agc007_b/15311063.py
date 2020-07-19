N=int(input())
p=list(map(int,input().split()))

ss=[1]*(N+1)
ss2=[-1]*(N+1)
ss[0]=0
ss2[0]=0
for i,x in enumerate(p[1:]):
  x-=1
  ss[x]+=i+1
  ss2[x+1]-=i+1

ac=[0]*(N+1)
ac2=[0]*(N+1)
ac[0]=1
ac2[0]=N**2
for i in range(N):
  ac[i+1]=ac[i]+ss[i]
  ac2[i+1]=ac2[i]+ss2[i]
print(*ac[1:])
print(*ac2[1:])

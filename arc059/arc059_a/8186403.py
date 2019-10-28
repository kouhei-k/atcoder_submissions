N=int(input())
a=list(map(int,input().split()))
ave=[sum(a)//N,sum(a)//N+1]
ans=[0,0]
for i in range(N):
  ans[0]+=(a[i]-ave[0])**2
  ans[1]+=(a[i]-ave[1])**2
print(min(ans))

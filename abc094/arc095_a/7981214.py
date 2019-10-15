N=int(input())
a=list(map(int,input().split()))
b=sorted(a)
ans=[b[N//2],b[(N//2) -1]]

for i in range(N):
  if a[i] >= ans[0]:
    print(ans[1])
  else:
    print(ans[0])

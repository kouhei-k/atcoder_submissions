N=int(input())
a=[-1]*(N+1)
for i in range(1,N+1):
  a[i]=int(input())
pos = 1
ans = 0
for _ in range(N):
  if pos == 2:
    print(ans)
    exit(0)
  pos = a[pos]
  ans += 1
  

print(- 1)

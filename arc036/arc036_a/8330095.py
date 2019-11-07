N,K=map(int,input().split())
t=[0]*N
for i in range(N):
  t[i]= int(input())
  if i>1:
    if K>t[i-2]+t[i-1]+t[i]:
      print(i+1)
      exit(0)
print(-1)

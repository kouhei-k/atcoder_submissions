N=int(input())
a=list(map(int,input().split()))
b=[[a[i],i+1] for i in range(N)]
b.sort(reverse = True, key=lambda x:x[0])
for i in range(N):
  print(b[i][1])

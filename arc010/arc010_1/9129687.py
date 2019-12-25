N,M,A,B=map(int,input().split())
c=[int(input()) for i in range(M)]

for i in range(M):
  if N<=A:
    N+=B
  if N>=c[i]:
    N-=c[i]
  else:
    print(i+1)
    exit(0)
print("complete")

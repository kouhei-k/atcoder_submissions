L,H=map(int,input().split())
N=int(input())
A=[int(input()) for i in range(N)]
for i in range(N):
  if A[i]>H:
    print(-1)
  elif A[i]>=L:
    print(0)
  else:
    print(L-A[i])

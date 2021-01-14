D, N = map(int, input().split())
T = [int(input()) for i in range(D)]
#それぞれの日で最小か最大かを選べばいい
ABC = [tuple(map(int, input().split())) for i in range(N)]
ans = -1
A=[]
for i in range(D):
  d=201
  u=0
  for a, b,c in ABC:
    if a<=T[i]<=b:
      if c<d:
        d=c
      if c>u:
        u=c
  A.append((u,d))
DP=[[0]*2 for i in range(D)]
    
for i in range(1,D):
  DP[i][0]=max(DP[i-1][0]+abs(A[i][0]-A[i-1][0]),DP[i-1][1]+abs(A[i][0]-A[i-1][1]))
  DP[i][1]=max(DP[i-1][0]+abs(A[i][1]-A[i-1][0]),DP[i-1][1]+abs(A[i][1]-A[i-1][1]))
print(max(DP[-1]))

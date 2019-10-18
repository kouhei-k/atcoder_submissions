N,M=map(int,input().split())
if N < M//2:
  ans=N
  M-=2*N
  ans+=M//4
  print(ans)
elif N==M//2:
  print(N)
else:
  print(M//2)
  

N,M=map(int,input().split())
L=[-1]*M
R=[-1]*M
for i in range(M):
  L[i],R[i] =map(int,input().split())
if min(R) >= max(L):
  print(min(R)-max(L)+1)
else:
  print(0)

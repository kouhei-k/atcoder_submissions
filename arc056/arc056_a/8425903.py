A,B,K,L=map(int,input().split())
if L*A<B:
  print(K*A)
else:
  k=K//L
  ans=k*B
  k=K%L
  if A*k < B:
    ans+=A*k
  else:
    ans+=B
  print(ans)

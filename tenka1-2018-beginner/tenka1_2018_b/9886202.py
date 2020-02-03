A,B,K=map(int,input().split())
flag=True
for i in range(K):
  if flag:
    flag=False
    A=A//2
    B+=A
  else:
    flag=True
    B=B//2
    A+=B
print(A,B)

N=int(input())
A=[int(input()) for i in range(N)]
maxa=max(A)
id=A.index(maxa)
for i in range(N):
  if i==id:
    tmp=max(A[:i]+A[i+1:])
    print(tmp)
  else:
    print(maxa)

A=[int(input()) for i in range(5)]
ans=0
if A[0]<0:
  ans-=A[0]*A[2] - A[3]
  A[0]=0
ans+= (A[1]-A[0])*A[-1]
print(ans)

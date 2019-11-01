A=int(input())
ans=0
for i in range(A+1):
  ans=max(i*(A-i),ans)
print(ans)

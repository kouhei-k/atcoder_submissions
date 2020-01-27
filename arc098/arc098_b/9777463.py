N=int(input())
A=list(map(int,input().split()))

s=[0]*(N+1)
xs=[0]*(N+1)
for i in range(N):
  s[i+1]=s[i]+A[i]
  xs[i+1]=xs[i] ^ A[i]
ans=0
l=0
for r in range(N+1):
    #print(l,r)
    
    if r == N:
      ans+=((r-l)*(r+1-l))//2
      continue   
    while(r != l):
      if s[r+1]-s[l] == xs[r+1]^xs[l]:
        break
      else:         
        ans+=r-l
        l+=1
print(ans)

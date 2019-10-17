import fractions
N,X=map(int,input().split())
x=list(map(int,input().split()))
diff = [abs(x[i]-X) for i in range(N)]
ans=diff[0]
for i in range(1,N):
  ans=fractions.gcd(ans,diff[i])
print(ans)

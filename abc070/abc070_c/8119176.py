N=int(input())
T=[int(input()) for i in range(N)]
import fractions
ans=1
for i in range(N):
  ans=ans*T[i]//fractions.gcd(ans,T[i])
print(ans)
  

K,A,B=map(int,input().split())
ans = K+1
if (K - (A-1)) %2==0:
  ans=max(ans,((K-(A-1))//2)*(B-A)+A)
else:
  ans=max(ans,((K-(A-1))//2)*(B-A)+A+1)
print(ans)

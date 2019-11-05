N,K=map(int,input().split())
import math
A=list(map(int,input().split()))
ans=1
ans+=math.ceil((N-K)/(K-1))
print(ans)

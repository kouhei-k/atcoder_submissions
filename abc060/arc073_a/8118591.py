N,T=map(int,input().split())
t=list(map(int,input().split()))
diff = [t[i]-t[i-1] for i in range(1,N)]
ans=T*N
for i in range(N-1):
  ans-=max((T - diff[i]),0)
print(ans)

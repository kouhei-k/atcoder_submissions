N=int(input())
A=list(map(int,input().split()))
B=[1 if A[i]%2==0 else 2 for i in range(N)]
ans=1
for i in range(N):
  ans*=3-B[i]
print(3**N - ans)

N=int(input())
S=[""]*N
P=[0]*N
for i in range(N):
  S[i],tmp=input().split()
  P[i]=int(tmp)
  
k=sum(P)
for i in range(N):
  if P[i]>k//2:
    print(S[i])
    exit(0)
print("atcoder")

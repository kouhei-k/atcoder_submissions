N,M=map(int,input().split())
A=[int(input()) for i in range(N)]
B=[int(input()) for i in range(M)]
B.sort()
point=[0]*N

for i,a in enumerate(A):
  while(B and a <= B[-1]):
    point[i]+=1
    B.pop()

ans=point.index(max(point)) +1
print(ans)

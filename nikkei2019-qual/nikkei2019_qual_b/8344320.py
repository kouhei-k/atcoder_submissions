N=int(input())
A=input()
B=input()
C=input()
count=[0]*N
for i in range(N):
  if A[i]!=B[i]:
    count[i]+=1
  if C[i]!=A[i] and C[i]!=B[i]:
    count[i]+=1
print(sum(count))

N,M=map(int,input().split())
A=[""]*N
B=[""]*M
for i in range(N):
  A[i]=input()
for i in range(M):
  B[i]=input()
  
A_tmp=[""]*M
for i in range(N-M+1):
  for j in range(N-M+1):
    for k in range(M):
      A_tmp[k]=A[j+k][i:i+M]
    if A_tmp==B:
      print("Yes")
      exit(0)

print("No")

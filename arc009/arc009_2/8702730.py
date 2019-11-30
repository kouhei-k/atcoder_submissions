A=list(map(int,input().split()))
N=int(input())
def func(A,str_num):
  B=[[A[i],i] for i in range(10)]
  B.sort(key=lambda x:x[0])
  ret=0
  for x in str_num:
    x=int(x)
    ret*=10
    ret+=B[x][1]
  return(ret)

C=[input() for i in range(N)]

D =[[func(A,C[i]), i] for i in range(N)]
D.sort(key=lambda x:x[0])


for i in range(N):
  print(C[D[i][1]])

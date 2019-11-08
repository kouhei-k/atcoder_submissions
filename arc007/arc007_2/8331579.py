N,M=map(int,input().split())
case=[i for i in range(N+1)]
disk=[i for i in range(N+1)]
for i in range(M):
  tmp=int(input())
  disk[case[0]],disk[tmp]=disk[tmp],0
  case[disk[case[0]]],case[0]=case[0],tmp
  
for i in range(1,N+1):
  print(case[i])
  

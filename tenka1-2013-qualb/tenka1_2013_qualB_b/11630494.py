import sys
input=sys.stdin.readline
Q,L=map(int,input().split())
l=0
s=[]
for _ in range(Q):
  query = tuple(input().split())
  if query[0]=="Size":
    print(l)
  elif query[0]=="Top":
    if l<=0:
      print("EMPTY")
      exit(0)
    print(s[-1][0])
  elif query[0]=="Push":
    N=int(query[1])
    M=int(query[2])
    l+=N
    if l>L:
      print("FULL")
      exit(0)
    s.append([M,N])
      
  else:
    N=int(query[1])
    l-=N
    if l<0:
      print("EMPTY")
      exit(0)
    while(N>0):
      if s[-1][1]>N:
        s[-1][1]-=N
        N=0
      else:
        N-=s[-1][1]
        s.pop()
print("SAFE")

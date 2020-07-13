def main():
  import sys
  input=sys.stdin.buffer.readline
  N,M=map(int,input().split())
  A=[list(map(int,input().split())) for i in range(N)]
  ans=N
  s=set()
  for i in range(M-1):
    d=[0]*M
    for j in range(N):
      for k in range(M):
        if A[j][k]-1 in s:
          continue
        else:
          d[A[j][k]-1]+=1
          break
    ans=min(ans,max(d))
    s.add(d.index(max(d)))
  print(ans)
main()
  

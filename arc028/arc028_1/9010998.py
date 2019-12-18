N,A,B=map(int,input().split())
while(N>0):
  N=max(N-A,0)
  if N==0:
    print("Ant")
    break
  N=max(N-B,0)
  if N==0:
    print("Bug")
    break

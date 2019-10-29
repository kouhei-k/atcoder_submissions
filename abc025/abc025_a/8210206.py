S=list(input())
N=int(input())
S.sort()
count=0
l=len(S)
if N%l>0:
  print(S[N//l]+S[N%l-1])
else:
  print(S[N//l - 1]+S[l-1])

N=int(input())
S=input()
if N%2==1:
  print(-1)
else:
  ans=0
  for a,b in zip(S[:N//2],S[N//2:]):
    if a!=b:
      ans+=1
  print(ans)

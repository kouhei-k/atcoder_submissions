S=input()
N=len(S)
ans=0
for i in range(N):
  if S[i]=="U":
    ans+=N-(i+1)
    ans+=i*2
  else:
    ans+=i
    ans+=(N-(i+1))*2
print(ans)

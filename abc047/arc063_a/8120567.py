S=input()
prev=S[0]
ans=0
for i in range(len(S)):
  if S[i] == prev:
    continue
  else:
    ans+=1
    prev=S[i]
print(ans)

S=input()
ans=S[0].upper()
if len(S)>1:
  ans+=S[1:].lower()
print(ans)

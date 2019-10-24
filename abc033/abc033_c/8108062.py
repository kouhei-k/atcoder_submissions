S=list(input().split("+"))
ans=0
for i in range(len(S)):
  if len(S[i])==1:
    if S[i]!="0":
      ans+=1
  else:
    tmp=1
    for x in S[i]:
      if x != "*":
        tmp*=int(x)
      
    if tmp!=0:
      ans+=1 
print(ans)

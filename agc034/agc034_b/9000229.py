S=input()
S=list(S.replace("BC","D"))
ans=0
count=0
for x in S:
  if x=="A":
    count+=1
  else:
    if x=="D":
      ans+=count
      continue
    else:
      count=0
print(ans)
  

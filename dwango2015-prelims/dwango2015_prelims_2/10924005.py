s=input()
s=list(s.replace("25","A"))
s.append("0")
l=0
ans=0
for x in s:
  if x == "A":
    l+=1
  else:
    ans+= (l *(l+1))//2
    l=0
print(ans)

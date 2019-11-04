s=input()
prev=s[0]
count=1
ans=[s[0]]
for i in range(1,len(s)):
  if s[i]== prev:
    count+=1
  else:
    ans.append(str(count))
    prev=s[i]
    ans.append(s[i])
    count=1
ans.append(str(count))
print("".join(ans))

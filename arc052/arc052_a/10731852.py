s=input()
ans=0

for x in s:
  if ord(x)>=48 and ord(x)<=58:
    ans*=10
    ans+=int(x)
print(ans)
  

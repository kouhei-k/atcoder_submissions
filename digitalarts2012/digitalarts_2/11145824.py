s=input()
if s == "z"*20 or s =="a":
  print("NO")
  exit(0)
alpha="abcdefghijklmnopqrstuvwxyz"
h=dict()
for i,x in enumerate(alpha):
  h[x]=i+1
v=0
for x in s:
  v+=h[x]
ans=[]
if s[0]==alpha[min(26,v)-1]:
  ans.append(alpha[min(26,v)-2])
  v-=min(26,v)-1
else:
  ans.append(alpha[min(26,v)-1])
  v-=min(26,v)
while(v>0):
  ans.append(alpha[min(26,v)-1])
  v-=min(26,v)
print("".join(ans))
  

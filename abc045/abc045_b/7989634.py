s=[list(input()) for i in range(3)]
for i in range(3):
  s[i]=list(reversed(s[i]))
flag=True
next=0
ans=0
mem_s=["a","b","c"]
ans_s=["A","B","C"]
while(flag):
  if len(s[next]) >0:
    tmp=s[next].pop()
    next=mem_s.index(tmp)
  else:
    ans=next
    flag=False
print(ans_s[ans])

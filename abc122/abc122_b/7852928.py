S=input()
acgt=["A","C","G","T"]
count=0
ans=0
for x in S:
  if x in acgt:
    count+=1
  else:
    count=0
  ans=max(ans,count)
print(ans)

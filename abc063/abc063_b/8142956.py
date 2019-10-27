import collections
table=collections.defaultdict(int)
s=input()
for x in s:
  table[x]+=1
  if table[x]>=2:
    print("no")
    exit(0)
print("yes")

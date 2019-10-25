import collections
table=collections.defaultdict(int)
for x in input():
  table[x]+=1
for x in table:
  if table[x]%2==1:
    print("No")
    exit(0)
print("Yes")

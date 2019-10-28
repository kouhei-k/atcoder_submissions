alphabet="abcdefghijklmnopqrstuvwxyz"
import collections
table=collections.defaultdict(int)
for x in input():
  table[x]+=1
for x in alphabet:
  if x in table:
    continue
  else:
    print(x)
    exit(0)
print("None")

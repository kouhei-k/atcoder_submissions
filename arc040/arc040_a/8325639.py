N=int(input())
import collections
table = collections.defaultdict(int)
for i in range(N):
  for x in input():
    table[x]+=1
r=0
b=0
if "R" in table:
  r=table["R"]
if "B" in table:
  b=table["B"]
if r>b:
  print("TAKAHASHI")
elif r<b:
  print("AOKI")
else:
  print("DRAW")

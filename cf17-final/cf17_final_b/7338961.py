import collections
S=input()
dic=collections.defaultdict(int)
for i in range(len(S)):
  dic[S[i]]+=1
smax=[0,"d"]
for i in dic:
  if dic[i] > smax[0]:
    smax=[dic[i],i]

if len(dic.values())==1:
  if len(S)==1:
    print("YES")
  else:
    print("NO")
  exit(0)
    
elif len(dic.values())==2:
  if len(S)==2:
    print("YES")
  else:
    print("NO")
  exit(0)
if sum(dic.values()) - smax[0]>= smax[0]:
  if smax[0] - min(dic.values()) <= 1:
    print("YES")
    exit(0)
    
print("NO")

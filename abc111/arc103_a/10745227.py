import collections
n=int(input())
v=list(map(int,input().split()))
odd=[v[i] for i in range(n) if i%2==0]
even=[v[i] for i in range(n) if i%2==1]
o=(collections.Counter(odd)).most_common()
e=(collections.Counter(even)).most_common()
o.append((0,0))
e.append((0,0))
if o[0][0]==e[0][0]:
  print(n-max(e[0][1]+o[1][1],e[1][1]+o[0][1]))
else:
  print(n-(e[0][1] +o[0][1]))

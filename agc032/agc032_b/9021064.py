import copy
N=int(input())
n=(N//2)*2
g=[set() for i in range(N)]
tmp={i for i in range(n)}
for i in range(n):
  g[i]=copy.copy(tmp)
  g[i].remove(i)
  g[i].remove(n-1-i)
count=0
if N%2!=0:
  g[N-1]=copy.copy(tmp)
  for i in range(N-1):
    g[i].add(N-1)
for i in range(N):
  count+=len(g[i])
print(count//2)

for i in range(N):
  for x in g[i]:
    print(i+1,x+1)
    g[x].remove(i)

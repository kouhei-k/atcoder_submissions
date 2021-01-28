N = int(input())
G= [set() for i in range(N)]
for i in range(N-1):
  a,b = map(int, input().split())
  a -= 1
  b -= 1
  G[a].add(b)
  G[b].add(a)
import collections
q = collections.deque()
q.append(0)
A = []
mod = 10**9 + 7
s = set([0])
G2 = [set() for i in range(N)]

while(q):
  x = q.popleft()
  A.append(x)
  for y in G[x]:
    if y in s:
      continue
    else:
      for z in G[y]:
        if z != x:
          G2[x].add(z)
      s.add(y)
      q.append(y)
B = [0]*N
for i in range(N-1,-1,-1):
  x = A[i]
  a = 1
  for y in G[x]:
    if B[y] > 0:
      a *= B[y]
  b = 1
  for y in G2[x]:
    if B[y] > 0:
      b *= B[y]
  B[x] = a + b
  B[x] %= mod

print(B[0])

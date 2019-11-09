import collections
N=int(input())
a=[-1]*(N+1)
checker = collections.defaultdict(int)
for i in range(1,N+1):
  a[i]=int(input())
pos = 1
checker[1] = 1
for _ in range(N):
  if pos == 2:
    print(len(checker.values()) - 1)
    exit(0)
  pos = a[pos]
  if pos not in checker:
    checker[pos] = 1
  else:
    break
  

print(- 1)

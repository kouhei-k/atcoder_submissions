import collections
N,M=map(int,input().split())

counter=collections.defaultdict(int)
for _ in range(N):
  text = list(input().split())
  for x in text[1:]:
    counter[x]+=1
ans=0
for x in counter:
  if counter[x]== N:
    ans+=1
print(ans)

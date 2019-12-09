import collections
s = input()
K = int(input())

abc = collections.defaultdict(list)

for i in range(len(s)):
  for j in range(1,K+1):
    if i+j <= len(s):
        abc[s[i:i+j]].append(i)


abc = list(abc.items())
abc.sort(key=lambda x: x[0])

print(abc[K-1][0])

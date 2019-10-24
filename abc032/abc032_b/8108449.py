S=input()
k=int(input())
import collections
table=collections.defaultdict(int)
for i in range(len(S)-k+1):
  table[S[i:k+i]]+=1
print(len(list(table.keys())))

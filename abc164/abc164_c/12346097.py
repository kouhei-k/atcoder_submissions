import collections
N = int(input())
S = [input() for i in range(N)]
C = collections.Counter(S)
print(len(C))

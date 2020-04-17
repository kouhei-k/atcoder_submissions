N,M=map(int,input().split())
A= list(map(int,input().split()))

import collections
C=collections.Counter(A).most_common()

if C[0][1]>N/2:
  print(C[0][0])
else:
  print("?")

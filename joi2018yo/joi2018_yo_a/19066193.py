from math import ceil
N,A,B,C,D = map(int, input().split())
print(min(B*ceil(N/A),D*ceil(N/C)))

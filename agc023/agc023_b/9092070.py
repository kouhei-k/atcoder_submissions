import collections
import sys
import numpy as np
input = sys.stdin.readline
table = collections.defaultdict(set)
N = int(input())
S = [list(input().rstrip()) for i in range(N)]
T = [[""] * (N*2) for i in range(2*N)]
table2 = [[set() for j in range(N)] for i in range(N)]

for i in range(2*N):
    if i < N:
        T[i] = S[i] + S[i]
    else:
        T[i] = S[i - N] + S[i-N]
ans = 0
T = np.array(T)
for i in range(N):
    tmp = T[i:i+N, N-1-i:2*N-1-i]

    if (tmp == tmp.T).all():
        ans += N - (N // 2)

    tmp = T[i+1:i+N+1, N-1-i:2*N-1-i]

    if (tmp == tmp.T).all():
        ans += N // 2
print(ans)

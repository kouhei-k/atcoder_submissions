import collections
N, P = map(int, input().split())
h = [int(input()) for i in range(N)]

sh = [0]*(N+1)
for i in range(N):
    sh[i+1] = sh[i] + h[i]

A = [0]*N
q = collections.deque()
S = 0

sh.append(0)
q.append(N)
A.append(1)
S = 1
mod = 1234567
for i in range(N):
    while(q and sh[i+1]-sh[q[0]+1] > P):
        S -= A[q.popleft()]
    A[i] = S
    S += A[i]
    S %= mod
    q.append(i)

print(A[-2] % mod)

import collections
N, L = map(int, input().split())

A = [int(input()) for i in range(N)]
A.append(-1)
A.append(-1)
B = [-1]*(N+2)
B[-1] = -1
B[-2] = -1
q = collections.deque()
for i in range(N):
    if A[i] > A[i-1] and A[i] > A[i+1]:
        q.append(i)
        B[i] = L - A[i]


while(q):
    x = q.popleft()
    A[x] = 0
    if A[x+1] and B[x+1] == -1 and A[x+1] > A[x+2]:
        B[x+1] = B[x] + L - A[x+1]
        q.append(x+1)
    if A[x-1] and B[x-1] == -1 and A[x-1] > A[x-2]:
        B[x-1] = B[x] + L - A[x-1]
        q.append(x-1)
print(max(B))

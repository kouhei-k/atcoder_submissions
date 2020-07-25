import sys
# print(sys.version)
N = int(input())

A = list(map(int, input().split()))

P = 1000
K = 0
for i in range(N-1):
    if A[i] < A[i+1]:
        K += P // A[i]
        P %= A[i]
    elif A[i] > A[i+1]:
        P += K*A[i]
        K = 0
P += K * A[-1]
print(P)

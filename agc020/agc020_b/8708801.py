import math
K = int(input())
A = list(map(int, input().split()))
N, n = 2, 2
k = [0, 0]
for i in reversed(range(K)):
    k[0] = (N // A[i])*A[i]
    k[1] = math.ceil(n / A[i]) * A[i]
    if k[0]*A[i] >= n and k[1] <= N:
        N = k[0]+A[i] - 1
        n = k[1]
    else:
        print(-1)
        exit(0)
print(n, N)

N, K, Q = map(int, input().split())

A = [0]*Q
for i in range(Q):
    A[i] = int(input())

B = [0]*N

for i in range(Q):
    B[A[i] - 1] += 1


for i in range(N):
    if K - (Q - B[i]) > 0:
        print("Yes")
    else:
        print("No")

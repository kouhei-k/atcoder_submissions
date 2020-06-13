N, K = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(K):
    tmp = [0] * (N+1)
    for i in range(N):
        tmp[max(0, i-A[i])] += 1
        tmp[min(N-1, i+A[i]) + 1] -= 1

    ans = [0]*N
    A[0] = tmp[0]
    for i in range(1, N):
        A[i] = A[i-1] + tmp[i]

    # print(*A)
    if sum(A) == N*N:
        break
print(*A)

import math
N, K = map(int, input().split())
mod = 10**9 + 7

if K < N:
    ans = 1
    for i in range(N, N+K):
        ans *= i
    for i in range(1, K+1):
        ans = (ans//i)
    print(ans % mod)
else:
    t = K // N
    r = K % N
    ans = 1
    for i in range(r):
        ans *= (N-i)
    for i in range(1, r+1):
        ans = (ans // i)

    print(ans % mod)

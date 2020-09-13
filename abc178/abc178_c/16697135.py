N = int(input())
ans = N*(N-1)
mod = 10**9 + 7
ans %= mod
ans = 1
A = 1
B = 1
C = 1
for i in range(N):
    A *= 10
    B *= 9
    C *= 8
    A %= mod
    B %= mod
    C %= mod

print((A-B*2+C) % mod)

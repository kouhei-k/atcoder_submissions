import fractions
import sys
input = sys.stdin.readline


P = 10**9 + 7
N = (10**6)+1
inv_t = [0]+[1]
for i in range(2, N):
    inv_t += [inv_t[P % i] * (P - int(P / i)) % P]

N = int(input())
A = tuple(map(int, input().split()))

mod = 10**9+7
lcm = 1
B = [0]*N

for i in range(N):
    lcm = (lcm // fractions.gcd(lcm, A[i])) * A[i]

ans = 0

lcm %= mod
for i in range(N):
    ans += (lcm * inv_t[A[i]]) % mod
    ans %= mod

print(ans)

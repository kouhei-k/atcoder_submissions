N, M, K = map(int, input().split())
mod = 998244353
ans = 0
tmp = M

P = mod
inv_t = [0]+[1]
# for i in range(2, M+1):
#     inv_t += [inv_t[P % i] * (P - int(P / i)) % P]


t = [0]*N
t[0] = M
for i in range(1, N):
    t[i] = t[i-1]*(M-1) % mod
# for i in range(K+1):
#     if i == 0:
#         ans += tmp
#     else:

#         tmp *= M-1-i
#         tmp *= inv_t[i]
#         tmp *= inv_t[M-1]
#         tmp %= mod
#         ans += tmp
#         ans %= mod
# print(ans)
MAX_N = N

fact = [1]
fact_inv = [0]*(MAX_N+4)
for i in range(MAX_N+3):
    fact.append(fact[-1]*(i+1) % mod)

fact_inv[-1] = pow(fact[-1], mod-2, mod)
for i in range(MAX_N+2, -1, -1):
    fact_inv[i] = fact_inv[i+1]*(i+1) % mod


def mod_comb_k(n, k, mod):
    return fact[n] * fact_inv[k] % mod * fact_inv[n-k] % mod


for i in range(K+1):
    ans += mod_comb_k(N-1, i, mod) * t[-1-i]


print(ans % mod)

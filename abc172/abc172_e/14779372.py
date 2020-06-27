N, M = map(int, input().split())
mod = 10**9 + 7

ans = M
for i in range(M-1, M-N, -1):
    ans = ans*i % mod


# print(ans)
prev = 1
ansB = M-1


for i in range(1, N):
    tmp = (prev)*i % mod
    tmp2 = ansB - tmp % mod
    # print(tmp2)
    ansB = tmp * (M-i) % mod
    ansB += (tmp2)*(M-i-1) % mod
    # print(tmp, tmp2)
    # ansB = tmp + tmp2
    ansB %= mod
    prev = tmp2
    # print(ansB)

# print(ansB)

print((ans*ansB) % mod)

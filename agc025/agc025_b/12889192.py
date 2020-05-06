N, A, B, K = map(int, input().split())
mod = 998244353
# AとBの組み合わせと、(A+B)と0の組み合わせが可換
# 順番というよりは個数の組み合わせがどうなるかの問題？
# 赤と青の個数の組み合わせは、(無色も含める？)


def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod


g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル


for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod//i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)
ans = 0
for i in range(N+1):
    D = (K - A*i)
    if D % B == 0 and D//B <= N:
        ans += cmb(N, i, mod) * cmb(N, D//B, mod)
        ans %= mod

print(ans)

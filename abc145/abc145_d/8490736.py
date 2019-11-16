X, Y = map(int, input().split())


def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod


mod = 10**9+7
N = 10**6
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

if X == Y // 2 or Y == X//2:
    print(1)
    exit(0)

X, Y = max(X, Y), min(X, Y)

diff = X - Y
x = X - 2*diff

if x % 3 != 0:
    print(0)
    exit(0)
else:
    k = x // 3
    for i in range(2, N + 1):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod//i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)

    ans = cmb(2*k+diff, k, mod)
    print(ans)

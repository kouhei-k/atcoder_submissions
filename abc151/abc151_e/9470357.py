import bisect
import collections


def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod


mod = 10**9+7  # 出力の制限
n = 10**6
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, n + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod//i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
mod = 10**9 + 7

table = collections.defaultdict(int)

for x in A:
    table[x] += 1
ans = 0
for x in table:
    # print(x)
    i = bisect.bisect_left(A, x)
    if i+table[x] >= K:
        for j in range(1, table[x] + 1):
            ans += cmb(i, K-j, mod)*x*cmb(table[x], j, mod)
            # print(ans, j)

    i = bisect.bisect_right(A, x)

    if N - (i-table[x]) >= K:
        for j in range(1, table[x] + 1):
            ans -= cmb(N-i, K-j, mod)*x*cmb(table[x], j, mod)
            # print(ans, j)
    ans %= mod
print(ans)

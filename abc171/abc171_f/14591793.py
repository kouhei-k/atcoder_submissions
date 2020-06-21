def main():
    import collections
    K = int(input())
    N = len(input())
    mod = 10**9 + 7

    def cmb(n, r, mod):
        if (r < 0 or r > n):
            return 0
        r = min(r, n-r)
        return g1[n] * g2[r] * g2[n-r] % mod

    n = N + K
    g1 = [1, 1]  # 元テーブル
    g2 = [1, 1]  # 逆元テーブル
    inverse = [0, 1]  # 逆元テーブル計算用テーブル

    for i in range(2, n + 1):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod//i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)

    d = [0]*(K+1)
    d[0] = 1
    d2 = [0]*(K+1)
    d2[0] = 1

    for i in range(K):
        d[i+1] = d[i]*26
        d[i+1] %= mod

        d2[i+1] = d2[i]*25
        d2[i+1] %= mod

    ans = 0
    for i in range(K+1):
        ans += d2[K-i] * d[i] * cmb(N+K-i-1, N-1, mod)
        ans %= mod
    print(ans)


main()

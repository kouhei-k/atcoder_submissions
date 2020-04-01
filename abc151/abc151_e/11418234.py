def main():
  import collections
  import bisect


  def cmb(n, r, mod):
      if (r < 0 or r > n):
          return 0
      r = min(r, n-r)
      return g1[n] * g2[r] * g2[n-r] % mod


  mod = 10**9+7  # 出力の制限
  N = 10**5
  g1 = [1, 1]  # 元テーブル
  g2 = [1, 1]  # 逆元テーブル
  inverse = [0, 1]  # 逆元テーブル計算用テーブル

  for i in range(2, N + 1):
      g1.append((g1[-1] * i) % mod)
      inverse.append((-inverse[mod % i] * (mod//i)) % mod)
      g2.append((g2[-1] * inverse[-1]) % mod)

  N, K = map(int, input().split())
  A = list(map(int, input().split()))
  table = collections.defaultdict(int)
  A.sort()
  for x in A:
      table[x] += 1
  ans = 0
  for x in table:
      left = bisect.bisect_left(A, x)
      for i in range(1, table[x]+1):
          if left >= K - i:
              ans += x * cmb(left, K - i, mod) * cmb(table[x], i, mod)

      right = left + table[x] - 1
      for i in range(1, table[x]+1):
          if N - 1 - right >= K - i:
              ans -= x * cmb(N - 1 - right, K-i, mod) * cmb(table[x], i, mod)
      ans %= mod
  print(ans)
main()

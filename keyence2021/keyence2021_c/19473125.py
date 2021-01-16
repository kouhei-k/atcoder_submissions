

def main():
    import math
    import sys
    input = sys.stdin.readline
    H, W, K = map(int, input().split())
    d = dict()
    for i in range(K):
        h, w, c = input().rstrip().split()
        h = int(h) - 1
        w = int(w) - 1
        d[(h, w)] = c
    DP = [[0]*(W+1) for i in range(H+1)]
    # 自分が通る可能性がなくて
    mod = 998244353
    def modinv(a, m):
      b = m
      x = 1
      y = 0
      while(b):
          t = a // b
          a -= t * b
          b, a = a, b
          x -= t * y
          x, y = y, x
      x %= m
      if x < 0:
          x += m
      return(x)
    Z = modinv(3,mod)
    a = pow(3, H*W-K, mod)
    DP[0][0] = a
    for i in range(H):
        for j in range(W):
            DP[i][j] %= mod
            r = DP[i][j]
            if (i, j) in d:
                x = d[(i, j)]
                if x == 'R':
                    DP[i][j+1] += r
                elif x == 'D':
                    DP[i+1][j] += r
                else:
                    DP[i][j+1] += r
                    DP[i+1][j] += r
            else:
                r *= Z
                DP[i][j+1] += r*2
                DP[i+1][j] += r*2
    ans = DP[H-1][W-1]
    print(ans%mod)


main()

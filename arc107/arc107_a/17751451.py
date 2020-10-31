a, b, c = map(int, input().split())
mod = 998244353

ans = a*(a+1) // 2
ans %= mod
ans *= b*(b+1) // 2
ans %= mod
ans *= c*(c+1) // 2
ans %= mod

print(ans)

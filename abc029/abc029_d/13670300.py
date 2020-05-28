N = int(input())
ans = 0
L = len(str(N))
for i in range(1, L+1):
    ans += N//(10**i) * (10**(i-1))
    k = N % (10**i)
    if k >= 2 * 10**(i-1):
        ans += 10**(i-1)
    else:
        ans += max(0, k+1 - 10**(i-1))
print(ans)

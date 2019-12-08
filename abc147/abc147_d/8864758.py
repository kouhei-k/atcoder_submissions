

N = int(input())
A = list(map(int, input().split()))

ans = 0
mod = 10**9 + 7


b = bin(max(A))

l = len(b) - 2


for j in range(l):
    tmp = 0
    for i in range(N):
        if (A[i] >> j) % 2 == 1:
            tmp += 1

    ans += (2**j) * tmp * (N-tmp)
    ans %= mod
print(ans)

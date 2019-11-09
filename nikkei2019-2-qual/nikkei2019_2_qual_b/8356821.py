import sys
input = sys.stdin.readline

N = int(input())
D = list(map(int, input().split()))
mod = 998244353

if 0 in D[1:] or D[0] != 0:
    print(0)
    exit(0)
else:
    num = [0]*max(D)
    for i in range(1, N):
        if D[i] > 0:
            num[D[i]-1] += 1

    ans = 1
    for i in range(1, len(num)):
        ans *= (num[i-1]**num[i]) % mod

    print(ans % mod)

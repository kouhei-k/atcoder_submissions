import bisect
N = int(input())
D = [0]*12
SD = [0]*12
tmp = 26
for i in range(1, 12):
    D[i] = tmp
    SD[i] = SD[i-1] + D[i]
    if SD[i] > 1000000000000001:
        break
    tmp *= 26


L = bisect.bisect_left(SD, N)
alpha = 'abcdefghijklmnopqrstuvwxyz'
ans = []
N -= SD[L-1] + 1
for i in range(L):
    ans.append(alpha[N % 26])
    N //= 26


print("".join(ans[::-1]))

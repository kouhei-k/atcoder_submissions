N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))

H = [[-1, 10**9] for i in range(N)]

prev = 0
for i, x in enumerate(T):
    if prev != x:
        if H[i][0] < 0:
            H[i][0] = x
        elif H[i][0] != x:
            print(0)
            exit(0)
    prev = x
    H[i][1] = min(H[i][1], x)
prev = 0
for i in range(N-1, -1, -1):
    x = A[i]
    if prev != x:
        if H[i][0] < 0:
            if H[i][1] >= x:
                H[i][0] = x
            else:
                print(0)
                exit(0)
        elif H[i][0] != x:
            print(0)
            exit(0)
    prev = x
    H[i][1] = min(H[i][1], x)
ans = 1
mod = 10**9 + 7
for x, y in H:
    if x > 0:
        continue
    else:
        ans *= y
        ans %= mod
print(ans)

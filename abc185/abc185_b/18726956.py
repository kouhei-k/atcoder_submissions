N, M, T = map(int, input().split())
t = 0
m = N
for _ in range(M):
    a, b = map(int, input().split())
    N -= (a - t)
    if N <= 0:
        print("No")
        exit(0)
    else:
        N += b - a
        N = min(N, m)
        t = b
if N > T - t:
    print("Yes")
else:
    print("No")

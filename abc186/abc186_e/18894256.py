import math
T = int(input())


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


for _ in range(T):
    N, S, K = map(int, input().split())
    B = N-S
    d = math.gcd(N, K)
    d = math.gcd(d, B)
    B //= d
    N //= d
    K //= d
    if math.gcd(N, K) != 1:
        print(-1)
    else:
        print((modinv(K, N)*B) % N)

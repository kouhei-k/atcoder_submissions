K = int(input())
if K % 2 == 0:
    print(-1)
else:
    mod = K
    t = 0
    for _ in range(K+1):
        t *= 10
        t += 7
        if t % mod == 0:
            print(_+1)
            exit(0)
        else:
            t %= mod
    print(-1)

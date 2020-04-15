N, M = map(int, input().split())
ab = [tuple(map(int, input().split())) for i in range(N)]

cd = [tuple(map(int, input().split())) for i in range(M)]


for a, b in ab:
    ret = -1
    dis = 10**20
    for i, x in enumerate(cd):
        c, d = x
        if dis > abs(c-a) + abs(d-b):
            dis = abs(c-a) + abs(d-b)
            ret = i
    print(ret+1)

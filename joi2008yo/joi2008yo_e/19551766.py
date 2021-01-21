R, C = map(int, input().split())
a = [list(map(int, input().split())) for i in range(R)]

A = 0
d = dict()
ans = 0
for i in range(2**R):
    J = set()
    tmp = 0
    for j in range(R):
        if (i >> j) % 2 == 1:
            J.add(j)
    for i in range(C):
        c = 0
        for j in range(R):
            x = a[j][i]
            if j in J:
                x ^= 1
            c += x
        tmp += max(c, R - c)
    if tmp > ans:
        ans = tmp
print(ans)

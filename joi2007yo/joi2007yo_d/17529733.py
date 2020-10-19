n = int(input())
m = int(input())
C = [i+1 for i in range(2*n)]
for i in range(m):
    k = int(input())
    if k == 0:
        for i, xy in enumerate(zip(C[:n], C[n:])):
            x, y = xy
            C[2*i] = x
            C[2*i+1] = y

    else:
        C = C[k:] + C[:k]

print(*C, sep='
')

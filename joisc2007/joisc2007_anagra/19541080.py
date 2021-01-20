S = list(input())
N = len(S)
A = [1]
for i in range(2, N+1):
    A.append(A[-1]*i)

B = sorted(S)

d = dict()
C = []
for x in S:
    if x not in C:
        C.append(x)
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

ans = 0
C.sort()

for i, x in enumerate(S[:-1]):
    l = N - 1 - i
    flag = True

    for y in C:
        a = A[l-1]
        if y == x:
            d[y] -= 1
            break
        if d[y] > 0:
            for z in d:
                k = d[z]
                if z == y:
                    k -= 1
                if k > 0:
                    a //= A[k-1]
            ans += a


print(ans+1)

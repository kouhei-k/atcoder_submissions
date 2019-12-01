from decimal import Decimal
T = tuple(map(Decimal, input().split()))

A = list(map(Decimal, input().split()))
B = list(map(Decimal, input().split()))


ans = 0
if A[0] < B[0]:
    tmp = (A[0], A[1])
    A[0], A[1] = B[0], B[1]
    B[0], B[1] = tmp[0], tmp[1]

a = abs(T[0]*A[0] - T[0]*B[0])

b = T[0]*(B[0]-A[0])+T[1]*(B[1]-A[1])


if b == 0:
    print("infinity")
elif b < 0:
    print(0)
    exit(0)
else:
    ans += 1
    if b > a:
        print(1)
    elif b == a:
        print("infinity")
    else:
        if a % b == 0:
            print((a//b)*2)
        else:
            print((a//b)*2 + 1)

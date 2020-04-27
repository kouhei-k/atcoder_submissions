A, B = map(int, input().split())

if A == B:
    print(A)
else:
    A -= 1
    ans = 0
    a = 1
    b = 1
    if ((A+1)//2) % 2 == 1:
        if A % 2 == 0:
            a = 1 ^ A
        else:
            a = 1
    else:
        if A % 2 == 1:
            a = 0
        else:
            a = A

    if ((B+1)//2) % 2 == 1:
        if B % 2 == 0:
            b = 1 ^ B
        else:
            b = 1
    else:
        if B % 2 == 1:
            b = 0
        else:
            b = B

    print(a ^ b)

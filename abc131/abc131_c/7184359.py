import fractions
A,B,C,D = map(int,input().split())

icm = int(C*D / fractions.gcd(C,D))
ans = (B - A + 1)
if A != B:
    if A % C == 0:
        ans -= int(B // C - A // C) + 1
    else:
        ans -= int(B // C - A // C)
    if A % D == 0:
        ans -= int(B // D - A // D) + 1
    else:
        ans -= int(B // D - A // D)

    if A % icm == 0:
        ans += int(B // icm - A // icm) + 1
    else:
        ans += int(B // icm - A // icm)
    print(int(ans))
else:
    if A % C == 0 or A % D == 0:
        print(0)
    else:
        print(1)

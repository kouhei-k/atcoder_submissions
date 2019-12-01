from decimal import Decimal, ROUND_HALF_UP
N = int(input())

X = 100*N // 108
# X = int((X+0.5)//1)
if (X * 1.08)//1 == N:
    print(X)

else:
    if ((X+1)*1.08) // 1 == N:
        print(X+1)
    else:
        print(":(")

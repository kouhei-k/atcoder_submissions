from decimal import *

getcontext().prec = 20      # デフォルト28桁のところを20桁にする

a, b, c = map(int, input().split())

A = Decimal(a).sqrt()
B = Decimal(b).sqrt()
C = Decimal(c).sqrt()
if A+B < C:
    print("Yes")
else:
    print("No")

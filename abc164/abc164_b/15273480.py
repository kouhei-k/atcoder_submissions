import math
A, B, C, D = map(int, input().split())

if math.ceil(C/B) > math.ceil(A/D):
    print("No")
else:
    print("Yes")

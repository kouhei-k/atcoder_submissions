import math
S = int(input())
a1, b2 = math.ceil(S**0.5), math.ceil(S**0.5)
c = a1*b2 - S

print("0 0 " + str(a1) + " " + str(c) + " 1 " + str(b2))

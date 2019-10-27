import math
a, b, x = map(int, input().split())
l = (a*a*b - x)/(a*a / 2)
if l <= b:
    k = math.degrees(math.atan2(l, a))
    print(k)
else:
    l = x/(a*b/2)
    k = 90.0 - math.degrees(math.atan2(l, b))
    print(k)

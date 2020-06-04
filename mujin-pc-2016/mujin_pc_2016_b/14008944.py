a,b,c = map(int, input().split())
a,b,c = sorted([a,b,c], reverse = True)
import math
p = math.pi
s1 = p * (a+b+c)**2
s2 = max(0, a - (b+c))**2 * p
print(s1 - s2)

import fractions
import math
a=int(input())
b=int(input())
n=int(input())

k = fractions.gcd(a,b)
k=a*b//k
print(math.ceil(n/k)*k)

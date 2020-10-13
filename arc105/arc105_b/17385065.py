import math
N = int(input())
a = list(map(int, input().split()))
x = a[0]
for y in a[1:]:
    x = math.gcd(x, y)
print(x)

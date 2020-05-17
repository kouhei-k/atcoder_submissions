import math
A, B, H, M = map(int, input().split())


b = (M * 6) % 360
H += M/60
a = (H * 30) % 360
deg = abs(a - b)

theta = math.radians(deg)


cc = (A**2 + B**2) - (2*A*B * math.cos(theta))

print(cc**0.5)

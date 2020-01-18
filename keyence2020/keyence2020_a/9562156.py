import math
H = int(input())
W = int(input())
N = int(input())

if H > W:
    H, W = W, H
print(math.ceil(N / W))

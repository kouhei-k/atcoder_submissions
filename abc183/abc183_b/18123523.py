Sx, Sy, Gx, Gy = map(int, input().split())

dx = Gx - Sx
dy = Gy + Sy

print(Sx + Sy * dx/dy)

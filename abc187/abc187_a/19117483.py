A, B = input().split()

a = 0
b = 0

for i in range(3):
    a += int(A[i])
    b += int(B[i])
print(max(a, b))

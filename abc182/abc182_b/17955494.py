N = int(input())
A = list(map(int, input().split()))

C = [0] * (max(A)+1)
for i in range(2, max(A)+1):
    for x in A:
        if x % i == 0:
            C[i] += 1
C[0] = -1
C[1] = -1
print(C.index(max(C)))

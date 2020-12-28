import bisect
n = int(input())
a = [int(input()) for i in range(n)]

A = []
for i in range(n):
    id = bisect.bisect_left(A, a[i])
    if id == len(A):
        A.append(a[i])
    else:
        A[id] = a[i]
print(len(A))

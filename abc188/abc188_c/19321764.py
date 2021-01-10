N = int(input())
A = list(map(int, input().split()))
X = max(A)

id = A.index(X)
Y = 0
if 2**(N-1) <= id:
    Y = max(A[:2**(N-1)])
else:
    Y = max(A[2**(N-1):])
print(A.index(Y) + 1)

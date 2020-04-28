N = int(input())
A = list(map(int, input().split()))

if abs(A[0]) < abs(A[-1]):
    A = A[::-1]
B = list(map(abs, A))
B.sort()
C = [x for x in A if x < 0]
n = len(C)
if n % 2 == 0:
    print(sum(B))
else:
    print(sum(B[1:]) - B[0])

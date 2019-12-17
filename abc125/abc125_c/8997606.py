import fractions
N = int(input())
A = list(map(int, input().split()))
B = [0]*N
B[0] = A[0]
for i in range(1, N-1):
    B[i] = fractions.gcd(A[i], B[i-1])

C = [0]*N
C[-1] = A[-1]
for i in reversed(range(1, N - 1)):
    C[i] = fractions.gcd(C[i+1], A[i])

ans = max(B[N-2], C[1])
for i in range(N-2):
    ans = max(ans, fractions.gcd(B[i], C[i+2]))
print(ans)

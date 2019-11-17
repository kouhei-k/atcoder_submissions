N = int(input())
A = [0]*N
B = [0]*N
a = [0]*(N+1)
for i in range(N):
    A[i], B[i] = map(int, input().split())
    a[i] = A[i]

ans = 0
for i in reversed(range(N)):
    k = (A[i] + ans) % B[i]
    if k != 0:
        k = B[i] - k
    ans += k
print(ans)

N = int(input())
A = list(map(int, input().split()))
A.sort()

S = [0]*(N+1)
for i in range(N):
    S[i+1] = S[i] + A[i]
ans = 0
k = N-1
for i in range(1, N):
    ans += S[N] - S[i] - A[i-1]*k
    k -= 1
print(ans)

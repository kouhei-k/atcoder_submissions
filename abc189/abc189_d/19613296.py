N = int(input())
S = [input() for i in range(N)]
ans = 0
A = [1]
for i in range(N):
    A.append(A[-1]*2)
for i in range(N)[::-1]:
    if S[i] == 'OR':
        ans += A[i+1]
print(ans+1)

N = int(input())
C = [int(input()) for i in range(N)]

A = [0]*N
B = [1]
for i in range(2,N):
    B.append(B[-1]*i)
ans = 0
for i in range(N):
    for j in range(N):
        if C[i] % C[j] == 0:
            A[i] += 1
    
    ans += (A[i] - A[i]//2)/A[i]

print(ans)

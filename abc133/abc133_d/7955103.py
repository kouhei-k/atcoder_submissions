N = int(input())
A = list(map(int, input().split()))

suma = sum(A)
tmp = 0
ans = [0] * N
for i in range(N):
    if i % 2 == 0:
        tmp += A[i]
ans[0] = (tmp*2) - suma
for i in range(N-1):
    ans[i+1] = (A[i] - (ans[i]//2))*2
print(" ".join(map(str, ans)))

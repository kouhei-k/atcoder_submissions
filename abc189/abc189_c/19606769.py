N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    S = A[i]
    if S > ans:
        ans = S
    for j in range(i+1, N):
        if S > A[j]:
            S = A[j]
        if S * (j+1 - i) > ans:
            ans = S*(j+1 - i)
print(ans)

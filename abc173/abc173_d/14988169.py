N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
k = N // 2

ans = sum(A[1:k]) * 2 + A[0]
if N % 2 == 1:
    ans += A[k]


print(ans)

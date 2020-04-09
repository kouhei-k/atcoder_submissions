A = list(map(int, input().split()))
A.sort()

ans = 0
if (A[2] - A[1]) % 2 == 0:
    ans += (A[2] - A[1]) // 2
else:
    A[0] += 1
    A[1] += 1
    ans += 1
    ans += (A[2] - A[1]) // 2
A[1] = A[2]

if (A[1] - A[0]) % 2 == 0:
    ans += (A[1] - A[0]) // 2
else:
    A[1] += 1
    A[2] += 1
    ans += 1
    ans += (A[1]-A[0])//2


print(ans)

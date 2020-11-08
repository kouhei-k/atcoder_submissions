A = list(input())
L = len(A)
A = list(map(int, A))

ans = L
for i in range(2**L):
    tmp = 0
    count = 0
    for j in range(L):
        if (i >> j) % 2 == 1:
            tmp += A[j]
        else:
            count += 1
    if (tmp % 3) == 0 and count < ans:
        ans = count
if ans == L:
    ans = -1
print(ans)
